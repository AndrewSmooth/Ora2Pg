import re


def oracle_unpivot_to_postgresql(original_sql):

    unpivot_pattern = re.compile(
        r'UNPIVOT\s*(?:\s*\(\s*(?:INCLUDE|EXCLUDE)\s*NULLS\s*\))?\s*\(\s*'
        r'(?P<value_column>\w+)\s+FOR\s+(?P<for_column>\w+)\s+'
        r'IN\s*\((?P<in_columns>[^)]+)\)\s*\)',
        re.IGNORECASE
    )

    match = unpivot_pattern.search(original_sql)
    if not match:
        return original_sql

    value_col = match.group('value_column')
    for_col = match.group('for_column')

    columns = []
    for col_part in match.group('in_columns').split(','):
        col_part = col_part.strip()
        if ' AS ' in col_part.upper():
            col, alias = re.split(r'\s+AS\s+', col_part, flags=re.IGNORECASE)
            columns.append((col.strip(' "\''), alias.strip(' "\'')))
        else:
            col = col_part.strip(' "\'')
            columns.append((col, col))

    values = [f"('{alias}', {col})" for col, alias in columns]
    values_str = ',\n        '.join(values)

    lateral_join = (
        f"\nJOIN LATERAL (VALUES\n"
        f"        {values_str}\n"
        f"    ) AS unpivoted({for_col}, {value_col}) ON true"
    )

    before = original_sql[:match.start()].rstrip()
    after = original_sql[match.end():].lstrip()

    result = f"{before}{lateral_join}{' ' + after if after else ''}"
    return re.sub(r'\n\s*\n', '\n', result)


