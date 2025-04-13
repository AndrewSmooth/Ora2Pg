import re

def sysdate_to_current_timestamp(oracle_sql):
    # паттерн для замены SYSDATE
    pattern = re.compile(r'\bSYSDATE\b', re.IGNORECASE)
    
    # замена на CURRENT_TIMESTAMP
    postgres_sql = pattern.sub('CURRENT_TIMESTAMP', oracle_sql)
    
    return postgres_sql