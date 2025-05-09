import re

pattern = r"""
    (.*?)                     # Текст до (нежадный)
    (                         # Целевой блок (жадный)
        (?:                   # Незахватываемая группа для DML
            UPDATE\s.*?;      |
            DELETE\s.*?;      |
            INSERT\s.*?;      |
            MERGE\s.*?;       
        )
        .*?                   # Любые символы до SQL%ROWCOUNT
        \bSQL%ROWCOUNT\b      # Целевой маркер
        .*?                   # Остаток блока до конца
        (?=                   # Опережающая проверка:
            \s*(?:UPDATE|DELETE|INSERT|MERGE|END|BEGIN|$)  # Следующий оператор или конец
        )
    )
    (.*)                      # Текст после
"""

def rowcount(oracle_sql: str):
    if not oracle_sql.strip():
        return oracle_sql
        
    result = []
    remaining = oracle_sql
    
    while True:
        match = re.search(pattern, remaining, re.IGNORECASE | re.VERBOSE | re.DOTALL)
        if not match:
            result.append(remaining)
            break
            
        before = match.group(1)
        target_block = match.group(2)
        after = match.group(3)
        
        # Разделяем DML операцию и часть с SQL%ROWCOUNT
        dml_part = target_block.split("SQL%ROWCOUNT")[0]
        rowcount_part = target_block[len(dml_part):]
        
        # Обрабатываем DML часть
        dml_statement = dml_part.split(";")[0] + ";"
        rest_of_dml = dml_part[len(dml_statement):]
        
        # Собираем результат
        result.append(before)
        result.append(dml_statement)
        result.append("\n  GET DIAGNOSTICS row_count = ROW_COUNT;")
        result.append(rest_of_dml)
        result.append(rowcount_part.replace("SQL%ROWCOUNT", "row_count"))
        
        remaining = after
    result[-1] = result[-1].replace("SQL%ROWCOUNT", "row_count")
    return "".join(result)

print(rowcount(oracle_sql = """
    BEGIN
        MERGE INTO target t
        USING source s ON (t.id = s.id)
        WHEN MATCHED THEN UPDATE SET t.value = s.value
        WHEN NOT MATCHED THEN INSERT (id, value) VALUES (s.id, s.value);
        
        processed_count := SQL%ROWCOUNT;
    END;
    """))