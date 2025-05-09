import re


def convert_sysdate_to_current_date(sql_query):
    pattern = re.compile(r'\bSYSDATE\b', re.IGNORECASE)
    converted_query = pattern.sub('CURRENT_DATE', sql_query)
    return converted_query
