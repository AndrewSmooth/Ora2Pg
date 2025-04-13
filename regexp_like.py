import re

def regexp_like_to_postgres(oracle_sql):
    # Паттерн для поиска REGEXP_LIKE в Oracle SQL
    pattern = re.compile(
        r'REGEXP_LIKE\s*\(\s*(?P<column>[a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*(?P<pattern>\'.*?\')\s*(?:,\s*\'(?P<modifier>[i]?)\'\s*)?\)',
        re.IGNORECASE
    )
    
    # callback-функция, которая вызывается для каждого совпадения в re.sub()
    def replacer(match):
        column = match.group('column')
        pattern = match.group('pattern')
        modifier = match.group('modifier') or ''
        
        # Определяем оператор для PostgreSQL
        operator = '~*' if 'i' in modifier.lower() else '~'
        
        return f"{column} {operator} {pattern}"
    
    # Заменяем все вхождения REGEXP_LIKE
    postgres_sql = pattern.sub(replacer, oracle_sql)
    
    return postgres_sql
