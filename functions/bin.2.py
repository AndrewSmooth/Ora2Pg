import re

def bin_to_num(sql):
    def replace_bin_to_num(match):
        args = match.group(1).split(',')
        args = [arg.strip() for arg in args]

        if all(arg.strip("' ") in ('0', '1') for arg in args):
            bit_string = ''.join(arg.strip("' ") for arg in args)
            return f"('{bit_string}'::bit({len(args)}))::integer"
        else:
            bit_expr = ' || '.join(args)
            return f"({bit_expr})::bit({len(args)})::integer"

    return re.sub(r'BIN_TO_NUM\s*\(([^)]+)\)', replace_bin_to_num, sql, flags=re.IGNORECASE)

