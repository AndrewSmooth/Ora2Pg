import re


def convert_oracle_to_postgres(sql):
    result = []
    i = 0
    n = len(sql)

    while i < n:
        if sql[i] == "'":
            result.append("'")
            i += 1
            while i < n:
                if sql[i] == "\\" and i + 1 < n:
                    result.append(sql[i:i + 2])
                    i += 2
                elif sql[i] == "'":
                    result.append("'")
                    i += 1
                    break
                else:
                    result.append(sql[i])
                    i += 1

        elif sql[i] == '"':
            result.append('"')
            i += 1
            while i < n:
                if sql[i] == "\\" and i + 1 < n:
                    result.append(sql[i:i + 2])
                    i += 2
                elif sql[i] == '"':
                    result.append('"')
                    i += 1
                    break
                else:
                    result.append(sql[i])
                    i += 1

        elif sql.startswith('--', i):
            start = i
            i += 2
            while i < n and sql[i] != '\n':
                i += 1
            result.append(sql[start:i])

        elif sql.startswith('/*', i):
            start = i
            i += 2
            while i < n - 1:
                if sql.startswith('*/', i):
                    i += 2
                    break
                else:
                    i += 1
            result.append(sql[start:i])

        else:
            start = i
            while i < n:
                if sql[i] in ("'", '"') or sql.startswith('--', i) or sql.startswith('/*', i):
                    break
                i += 1
            code_part = sql[start:i]
            code_part = re.sub(r'\bMINUS\b', 'EXCEPT', code_part, flags=re.IGNORECASE)
            result.append(code_part)

    return ''.join(result)