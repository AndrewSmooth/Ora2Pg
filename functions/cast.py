import re


def number_to_cast(sql):
    pattern = r'TO_NUMBER\((.*?)\)'

    def replace_match(match):
        value = match.group(1).strip()
        return f"CAST({value} AS NUMERIC)"

    pg_query = re.sub(pattern, replace_match, sql, flags=re.IGNORECASE)

    return pg_query







