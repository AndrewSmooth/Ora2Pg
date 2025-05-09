def instr_to_position(sql_query):

    def find_matching_paren(s, start):
        depth = 0
        for i in range(start, len(s)):
            if s[i] == '(':
                depth += 1
            elif s[i] == ')':
                depth -= 1
                if depth == 0:
                    return i
        return -1  # ошибка

    def split_instr_args(arg_str):
        depth = 0
        in_string = False
        for i, c in enumerate(arg_str):
            if c == "'" and (i == 0 or arg_str[i - 1] != "\\"):
                in_string = not in_string
            elif not in_string:
                if c == '(':
                    depth += 1
                elif c == ')':
                    depth -= 1
                elif c == ',' and depth == 0:
                    return arg_str[:i].strip(), arg_str[i + 1:].strip()
        return None, None

    result = ''
    i = 0
    while i < len(sql_query):
        if sql_query[i:i + 5].upper() == 'INSTR' and i + 5 < len(sql_query) and sql_query[i + 5] == '(':
            start = i + 6
            end = find_matching_paren(sql_query, i + 5)
            if end == -1:
                result += sql_query[i]
                i += 1
                continue

            args_str = sql_query[start:end]
            haystack, needle = split_instr_args(args_str)
            if haystack and needle:
                converted = f"POSITION({needle} IN {haystack})"
                result += converted
            else:
                # некорректный вызов
                result += sql_query[i:end + 1]

            i = end + 1
        else:
            result += sql_query[i]
            i += 1

    return result

