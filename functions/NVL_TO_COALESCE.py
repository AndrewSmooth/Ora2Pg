import re

def nvl_to_coalesce(query):
    pattern = re.compile(
        r'NVL\s*\(\s*((?:[^()]|\((?:[^()]|\([^()]*\))*\))*)\s*,\s*((?:[^()]|\((?:[^()]|\([^()]*\))*\))*)\s*\)',
        re.IGNORECASE | re.DOTALL
    )
    
    while True:
        new_query = pattern.sub(r'COALESCE(\1, \2)', query)
        if new_query == query:
            break
        query = new_query
    
    return query