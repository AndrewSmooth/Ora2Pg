import re


def dbms_random_to_random(sql_query):
    # Заменяем DBMS_RANDOM.VALUE() на RANDOM()
    sql_query = re.sub(
        r'DBMS_RANDOM\.VALUE\s*\(\s*\)',
        'RANDOM()',
        sql_query,
        flags=re.IGNORECASE
    )
    
    # Заменяем DBMS_RANDOM.VALUE(low, high) на (low + (high-low)*RANDOM())
    sql_query = re.sub(
        r'DBMS_RANDOM\.VALUE\s*\(\s*([^,]+)\s*,\s*([^,]+)\s*\)',
        r'(\1 + ((\2 - \1) * RANDOM()))',
        sql_query,
        flags=re.IGNORECASE
    )
    
    # Заменяем DBMS_RANDOM.NORMAL() на RANDOM()
    sql_query = re.sub(
        r'DBMS_RANDOM\.NORMAL\s*\(\s*\)',
        'RANDOM()',
        sql_query,
        flags=re.IGNORECASE
    )
    
    return sql_query