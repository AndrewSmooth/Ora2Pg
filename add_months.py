import re


def convert_oracle_add_months_to_postgresql(sql_query):
    pattern = re.compile(
        r'(?i)\bADD_MONTHS\s*\(\s*([^,]+)\s*,\s*([^)]+)\s*\)',
        re.IGNORECASE
    )

    def replacer(match):
        date_expr = match.group(1).strip()
        months = match.group(2).strip()
        return f"({date_expr} + INTERVAL '{months} months')"

    converted_query = pattern.sub(replacer, sql_query)
    return converted_query
