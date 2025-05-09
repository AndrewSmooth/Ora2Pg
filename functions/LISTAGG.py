import re

def listagg_to_string_agg(sql_query):

    # с сортировкой
    sql_query = re.sub(
        r'LISTAGG\s*\(\s*(.*?)\s*,\s*(.*?)\s*\)\s*WITHIN\s+GROUP\s*\(\s*ORDER\s+BY\s+(.*?)\s*\)',
        lambda m: f'STRING_AGG({m.group(1).strip()}, {m.group(2).strip()} ORDER BY {m.group(3).strip()})',
        sql_query,
        flags=re.IGNORECASE
    )
    
    # без сортировки
    sql_query = re.sub(
        r'LISTAGG\s*\(\s*(.*?)\s*,\s*(.*?)\s*\)',
        lambda m: f'STRING_AGG({m.group(1).strip()}, {m.group(2).strip()})',
        sql_query,
        flags=re.IGNORECASE
    )
    
    return sql_query




