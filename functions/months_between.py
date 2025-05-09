import re

def months_between(sql_query):

    return re.sub(
        r'MONTHS_BETWEEN\s*\(\s*(.*?)\s*,\s*(.*?)\s*\)',
        lambda m: f"((EXTRACT(YEAR FROM AGE({m.group(1).strip()}, {m.group(2).strip()})) * 12) + EXTRACT(MONTH FROM AGE({m.group(1).strip()}, {m.group(2).strip()})))",
        sql_query,
        flags=re.IGNORECASE
    )