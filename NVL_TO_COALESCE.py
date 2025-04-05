import re

def nvl_to_coalesce(query):
    query = re.sub(r"NVL\(\s*([^,]+)\s*,\s*([^,]+)\s*\)", r"COALESCE(\1, \2)", query)
    
    return query