import re

def subtstr_to_substring(sql_query):
    pattern = r'SUBSTR\s*\(\s*([^,]+)\s*,\s*([^,]+)\s*(?:,\s*([^)]+))?\s*\)'
    
    def replacement(match):
        string = match.group(1).strip()
        start = match.group(2).strip()
        length = match.group(3).strip() if match.group(3) else None
        
        if length:
            return f"SUBSTRING({string} FROM {start} FOR {length})"
        else:
            return f"SUBSTRING({string} FROM {start})"
    
    return re.sub(pattern, replacement, sql_query, flags=re.IGNORECASE)
