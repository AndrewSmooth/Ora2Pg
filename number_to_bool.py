import re

def number1_to_boolean(sql_query):


    pattern = r'NUMBER\s*\(\s*1\s*\)'

    return re.sub(
        pattern,
        'BOOLEAN',
        sql_query,
        flags=re.IGNORECASE 
    )