import re


def instr_to_position(query):

    def replace_instr(match):
        parts = match.group(1).split(',')
        string = parts[0].strip()
        substring = parts[1].strip()
        return f"POSITION({substring} IN {string})"


    pg_query = re.sub(r'INSTR\((.*?)\)', replace_instr, query, flags=re.IGNORECASE)

    return pg_query

