import re
import sqlparse


oracle_to_postgres_types = [
    ("BINARY_FLOAT", "REAL"),
    ("BINARY_DOUBLE", "DOUBLE PRECISION"),
    ("BINARY_INTEGER", "INTEGER"),
    ("VARCHAR2(n)", "VARCHAR(n)"),
    ("CHAR(n)", "CHAR(n)"),
    ("DATE", "TIMESTAMP(0)"),
    ("TIMESTAMP", "TIMESTAMP"),
    ("CLOB", "TEXT"),
    ("BLOB", "BYTEA"),
    ("RAW(n)", "BYTEA"),
    ("LONG", "TEXT"),
    ("INTERVAL YEAR TO MONTH", "INTERVAL YEAR TO MONTH"),
    ("INTERVAL DAY TO SECOND", "INTERVAL DAY TO SECOND"),
    ("BOOLEAN", "BOOLEAN"),
]

def convert_data_types(sql_query):
    converted_query = sql_query

    converted_query = re.sub(
        r'\bNUMBER\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)',
        r'NUMERIC(\1,\2)',
        converted_query,
        flags=re.IGNORECASE
    )

    converted_query = re.sub(
        r'\bNUMBER\s*\(\s*(\d+)\s*\)',
        r'NUMERIC(\1)',
        converted_query,
        flags=re.IGNORECASE
    )

    converted_query = re.sub(
        r'\bNUMBER\b',
        'NUMERIC',
        converted_query,
        flags=re.IGNORECASE
    )

    for oracle_type, postgres_type in oracle_to_postgres_types:
        if "(n)" in oracle_type:
            base = oracle_type.split("(")[0]
            pg_base = postgres_type.split("(")[0]
            pattern = rf'\b{base}\s*\(\s*\d+\s*\)'
            converted_query = re.sub(
                pattern,
                lambda m: re.sub(base, pg_base, m.group(), flags=re.IGNORECASE),
                converted_query,
                flags=re.IGNORECASE
            )
        else:
            pattern = rf'\b{re.escape(oracle_type)}\b'
            converted_query = re.sub(pattern, postgres_type, converted_query, flags=re.IGNORECASE)

    return sqlparse.format(converted_query, reindent=True, keyword_case='upper')





