import re


# Регулярные выражения для извлечения всех компонентов
patterns = {
    'target_table': r"MERGE\s+INTO\s+([^\s]+)\s+([^\s\(\)]+)", # целевая таблица
    'source_table': r"USING\s+([^\s]+)\s+([^\s\(\)]+)", # исходная таблица
    'on_condition': r"ON\s*\(([^)]+)\)", # условие
    'matched_action': r"WHEN\s+MATCHED\s+THEN\s+(.*?)(?=\s*WHEN\s+NOT\s+MATCHED|\s*;)", # действия если условие выполнено
    'not_matched_action': r"WHEN\s+NOT\s+MATCHED\s+THEN\s+(.*?)(?=\s*;)" # если не выполнено
}


def merge_to_delete_update_insert(oracle_sql: str, use_update: bool):
    postgres_sql = ""
    result = None
    if "MERGE" in oracle_sql or "merge" in oracle_sql:
        result = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, oracle_sql, re.IGNORECASE | re.DOTALL)
            if match:
                if key in ['target_table', 'source_table']: # если парсим названия таблиц, находим их алиасы
                    result[key] = match.group(1)
                    result[f"{key}_alias"] = match.group(2)
                else:
                    result[key] = match.group(1).strip()  # остальные компоненты

    
    # подготовка update и insert
    
    # Проверяем есть ли DELETE в HAS MATCHED и извлекаем его аргументы
    matched_block = re.search(r'WHEN\s+MATCHED\s+THEN\s+(.*?)(?=\s*WHEN\s+NOT\s+MATCHED|\s*;)', oracle_sql, re.IGNORECASE | re.DOTALL)
    delete_match = False
    if matched_block:
        delete_match = re.search(r'DELETE\s+WHERE\s+([^;]+?(?=\s*(?:WHEN|;|$)))', matched_block.group(1), re.IGNORECASE)
    deletion_args = delete_match.group(1).strip() if delete_match else None

    # Проверяем на дополнительное условие WHERE для update
    extra_condition = None
    extra_condition_pattern = r'UPDATE\s+SET\b.*?WHERE\s+(.*?)(?=\s*WHEN\s|\s*;)'
    if re.search(extra_condition_pattern, oracle_sql, re.IGNORECASE | re.DOTALL): 
        condition_match = re.search(extra_condition_pattern, oracle_sql, re.IGNORECASE | re.DOTALL)
        if condition_match:
            extra_condition = condition_match.group(1).strip()
    
    # Проверяем на дополнительное условие WHERE для insert
    extra_condition_insert = None
    extra_condition_pattern_insert = r'VALUES\b.*?\bWHERE\b'
    if re.search(extra_condition_pattern_insert, oracle_sql, re.IGNORECASE): 
        condition_match_insert = re.search( r'VALUES\b.*?\bWHERE\s+(.*?)(?=\s*(?:WHEN|;|$))', oracle_sql, re.IGNORECASE)
        if condition_match:
            extra_condition_insert = condition_match_insert.group(1)
    
    # парсинг названий изменяемых столбцов в update
    update_matches = re.findall(r'UPDATE SET\s+(.*?)(?=\s*WHEN NOT MATCHED|\s*;|\s*DELETE|\s*$)', oracle_sql, re.IGNORECASE | re.DOTALL)
    attributes = []
    if update_matches:
        # Разбиваем на отдельные присваивания
        assignments = [a.strip() for a in update_matches[0].split(',')]
        
        # Извлекаем атрибуты (левые части присваиваний)
        for assignment in assignments:
            # Ищем паттерн "таблица.атрибут" в левой части
            match = re.search(r'([a-z])\.([a-z_]+)\s*=', assignment, re.IGNORECASE)
            if match:
                attributes.append(match.group(2))  # group(2) - имя атрибута
    
    # парсинг названий изменяемых столбцов в insert
    insert_args_pattern = r'''
        WHEN\s+NOT\s+MATCHED\s+THEN
        \s*INSERT\s*\(\s*((?:[^,)]+(?:\s*,\s*[^,)]+)*)\s*)\)  # Колонки
        \s*VALUES\s*\(\s*((?:[^,)]+(?:\s*,\s*[^,)]+)*)\s*)\)  # Значения
    '''
    match = re.search(insert_args_pattern, oracle_sql, re.IGNORECASE | re.VERBOSE)
    insert_args = {}
    if match:
        columns = [col.strip() for col in re.split(r'\s*,\s*', match.group(1))]
        values = [val.strip() for val in re.split(r'\s*,\s*', match.group(2))]
        insert_args = dict(zip(columns, values))
        # print(insert_args)

    if result:
        update = None
        delete = None
        # сборка postgres запроса
        if use_update:
            update = translate_update(
                result["target_table"],
                result["target_table_alias"],
                result["source_table"],
                result["source_table_alias"],
                result["on_condition"],
                extra_condition,
                deletion_args,
                attributes
            )
        else:
            delete = translate_delete(
                result["target_table"],
                result["target_table_alias"],
                result["source_table"],
                result["source_table_alias"],
                result["on_condition"],
                extra_condition,
                deletion_args,
                attributes
            )
        insert = translate_insert(
            use_update,
            result["target_table"],
            result["target_table_alias"],
            result["source_table"],
            result["source_table_alias"],
            result["on_condition"],
            extra_condition_insert,
            insert_args,
        )
        postgres_sql = ""
        if update:
            postgres_sql += update
        elif delete:
            postgres_sql += delete
        print(insert)
        postgres_sql +=("\n\n"+insert)
        return postgres_sql
    else: 
        return None
    



def translate_update(tt: str, tt_a: str, st: str, st_a: str, condition: str, extra_condition: str, deletion_args: str, attributes: list):
    begin_string = f"UPDATE {tt} AS {tt_a}\n"
    end_string = f"FROM {st} AS {st_a}\nWHERE {condition}"
    
    # простое обновление (1 поле)
    if len(attributes) == 1:
        middle_string = f"SET {attributes[0]} = {st_a}.{attributes[0]}\n"
    
    # обновление нескольких полей
    if len(attributes) > 1:
        middle_string = f"SET\n"
        for i in range(len(attributes)):
            middle_string += f"    {attributes[i]} = {st_a}.{attributes[i]}\n"

    # обновление с условием WHERE
    if extra_condition:
        end_string += f" AND {extra_condition}"

    middle_string = ""
    # обновление с удалением
    if deletion_args:
        pattern = r'^\(?([A-Za-z])\.'
        match = re.search(pattern, deletion_args)
        table = tt 
        alias = tt_a
        if match: # если в удалении не целевая таблица, меняем table и alias
            alias = match.group(1) # если таблица не указана, будет целевая
            if alias == st_a:
                table = st 
        middle_string += f"\nDELETE FROM {table} AS {alias}\nWHERE {deletion_args}\nAND {tt_a}.id IN(\nSELECT {st_a}.id FROM {st} {st_a} WHERE {st_a}.id = {tt_a}.id\n);\n"

    return begin_string+middle_string+end_string+";"

def translate_delete(tt: str, tt_a: str, st: str, st_a: str, condition: str, extra_condition: str, deletion_args: str, attributes: list):
    begin_string = f"DELETE FROM {tt} AS {tt_a}\n WHERE EXISTS ("
    end_string = f"\n)"
    
    middle_string = f"\n\tSELECT 1 FROM {st} AS {st_a}\n\tWHERE {condition}"

    # удаление с условием WHERE
    if extra_condition:
        middle_string += f" AND {extra_condition}"

    return begin_string+middle_string+end_string+";"

def translate_insert(use_update, tt:str, tt_a: str, st:str, st_a: str, condition:str, extra_condition: str, insert_args: dict):
    keys_str = ""
    values_str = ""
    values_delimiter = ", "
    if len(insert_args.keys())>3:
        values_delimiter = ",\n    "
    for key, value in insert_args.items():
        keys_str += key + ", "
        values_str += value + values_delimiter

    begin_string = f"INSERT INTO {tt} ({keys_str[:-2]})\n"
    sub_end_string = f"\nFROM {st} AS {st_a}\n"
    end_string = f"WHERE NOT EXISTS (\nSELECT 1 FROM {tt} {tt_a} WHERE {condition}\n);"
    # простая вставка
    middle_string = f"SELECT {values_str[:-2]}"

    # вставка с условием WHERE
    if extra_condition:
        sub_string += f"{extra_condition+"\nAND "}"
    if use_update:
        return begin_string + middle_string + sub_end_string + end_string
    else:
        return begin_string + middle_string + sub_end_string

    