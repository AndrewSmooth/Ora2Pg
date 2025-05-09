import re

patterns = {
    'column': r"DECODE\(\s*([^,]+)", # столбец для проверки значений
    'args': r"DECODE\([^,]+\s*,\s*(.*?)\s*\)",
}

def decode_to_case(oracle_sql: str):
    result = 'CASE '
    if "DECODE" in oracle_sql or "decode" in oracle_sql:
        # Извлечение имени столбца
        column_match = re.search(patterns['column'], oracle_sql)
        column = column_match.group(1) if column_match else None
        if column:
            result += column+'\n'
        # Извлечение всех аргументов
        args_match = re.search(patterns['args'], oracle_sql)
        args = [arg.strip().strip("'") for arg in re.split(r"\s*,\s*", args_match.group(1))] if args_match else []
        for j in range(len(args)):
            try:
                flag = args[j] == float(args[j])
            except:
                args[j] = "'" + args[j] + "'"
        print(args)
        if args:
            for i in range(0, int(len(args)/2)*2, 2):
                result += f'\t\tWHEN {args[i]} THEN {args[i+1]}\n'
            result += f"\t\tELSE {args[-1]}\n\tEND"

    postgres_sql = re.sub(r'DECODE\(([^)]+)\)', result, oracle_sql)
    return postgres_sql

# print(decode_to_case(sql))