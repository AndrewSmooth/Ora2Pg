import re


def convert_trunk_to_date_trunc(sql_query):
    pattern = r'trunk\s*\(\s*([^,]+)\s*,\s*\'([^\']+)\'\s*\)'

    def replacer(match):
        date_part = match.group(1)
        unit = match.group(2).lower()
        unit_mapping = {
            'year': 'year',
            'yyyy': 'year',
            'yy': 'year',
            'month': 'month',
            'mm': 'month',
            'mon': 'month',
            'day': 'day',
            'dd': 'day',
            'hour': 'hour',
            'hh': 'hour',
            'minute': 'minute',
            'mi': 'minute',
            'second': 'second',
            'ss': 'second',
            'week': 'week',
            'ww': 'week'
        }
        pg_unit = unit_mapping.get(unit, unit)
        return f"date_trunc('{pg_unit}', {date_part})"

    converted_query = re.sub(pattern, replacer, sql_query, flags=re.IGNORECASE)

    return converted_query

