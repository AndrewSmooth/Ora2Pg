import re


patterns = {
    "refcursor": r'\bSYS_REFCURSOR\b',
    "return": r'\bRETURN\s+REFCURSOR\b',
    "in_out": r'(\w+)\s+IN\s+OUT\s+REFCURSOR\b',
    "no_found": r'%\s*NOTFOUND\b',
    "rowtype": r'(\w+)\s*%\s*ROWTYPE\b(?!\s*IS\s*TABLE)',
    "put_line": r'\bDBMS_OUTPUT\.PUT_LINE\b',
    "assigment": r'(\w+)\s*:=\s*(\w+)\s*\(([^)]*)\)\s*;',
}


def refcursor(oracle_code):
    # Заменяем SYS_REFCURSOR на REFCURSOR
    postgres_code = re.sub(patterns["refcursor"], 'REFCURSOR', oracle_code, flags=re.IGNORECASE)
    
    # Заменяем RETURN SYS_REFCURSOR на RETURNS REFCURSOR
    postgres_code = re.sub(patterns["return"], 'RETURNS REFCURSOR', postgres_code, flags=re.IGNORECASE)

    # Соединение IN OUT, Меняем местами INOUT и REFCURSOR 
    postgres_code = re.sub(patterns["in_out"], r'INOUT \1 REFCURSOR', postgres_code, flags=re.IGNORECASE)
    
    # Заменяем %NOTFOUND на NOT FOUND
    postgres_code = re.sub(patterns["no_found"], 'NOT FOUND', postgres_code, flags=re.IGNORECASE)
    
    # Заменяем %ROWTYPE на RECORD (только для переменных курсора)
    postgres_code = re.sub(patterns["rowtype"], r'RECORD', postgres_code, flags=re.IGNORECASE)
    
    # Заменяем DBMS_OUTPUT.PUT_LINE на RAISE NOTICE
    postgres_code = re.sub(patterns["put_line"], 'RAISE NOTICE', postgres_code, flags=re.IGNORECASE)

    # CALL вместо присваивания
    postgres_code = re.sub(patterns["assigment"], \
        lambda m: f"CALL {m.group(2)}({m.group(3)}{',' if m.group(3) else ''} {m.group(1)});", \
        postgres_code, flags=re.IGNORECASE)
    
    # Меняем IS на AS
    postgres_code = re.sub(r'\bIS\s*$', 'AS $$', postgres_code, flags=re.IGNORECASE)

    postgres_code = re.sub(r'\(\s*,', '(', postgres_code)  # Удаляет пробелы перед запятой
    postgres_code = re.sub(r',\s*\)', ')', postgres_code)  # Удаляет пробелы после запятой

    # Удаляем пробелы после открывающей скобки в вызовах CALL
    postgres_code = re.sub(r'CALL (\w+)\(\s+(\w+)', r'CALL \1(\2', postgres_code)

    # Удаляем пробелы перед закрывающей скобкой в вызовах CALL
    postgres_code = re.sub(r'(\w+)\s+\)', r'\1)', postgres_code)
    
    return postgres_code