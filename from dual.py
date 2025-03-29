import re


def convert_from_dual(oracle_query):
    postgres_query = re.sub(
        r'FROM\s+DUAL\s*;?\s*$',
        '',
        oracle_query,
        flags=re.IGNORECASE
    )

    postgres_query = re.sub(
        r'FROM\s+DUAL\s+(WHERE|GROUP BY|HAVING|ORDER BY|LIMIT|OFFSET|FETCH|FOR)',
        r'\1',
        postgres_query,
        flags=re.IGNORECASE
    )

    postgres_query = re.sub(
        r'^\(\s*(SELECT\s+.+?)\s*\)\s*$',
        r'\1',
        postgres_query,
        flags=re.IGNORECASE | re.DOTALL
    )

    if postgres_query.strip().upper().startswith('SELECT ') and ' FROM ' not in postgres_query.upper():
        pass

    return postgres_query.strip()