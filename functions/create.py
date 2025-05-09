import re

def convert_oracle_procedure_to_postgresql_function(oracle_sql: str) -> str:

    proc_name_match = re.search(r'CREATE\s+OR\s+REPLACE\s+PROCEDURE\s+(\w+)', oracle_sql, re.IGNORECASE)
    proc_name = proc_name_match.group(1) if proc_name_match else "unnamed_function"

    params_match = re.search(r'\((.*?)\)\s+AS', oracle_sql, re.IGNORECASE | re.DOTALL)
    params = params_match.group(1).strip() if params_match else ""

    param_list = []
    out_params = []
    if params:
        param_lines = [p.strip() for p in params.split(",")]
        for param in param_lines:
            param_parts = param.split()
            param_name = param_parts[0]
            direction = param_parts[1].upper() if len(param_parts) > 2 else "IN"
            data_type = param_parts[-1]

            if data_type.upper() == "NUMBER":
                pg_type = "NUMERIC"
            elif data_type.upper() == "VARCHAR2":
                pg_type = "VARCHAR"
            elif data_type.upper() == "DATE":
                pg_type = "TIMESTAMP"
            else:
                pg_type = data_type

            if direction == "OUT":
                out_params.append((param_name, pg_type))
            else:
                param_list.append(f"{param_name} {pg_type}")

    if len(out_params) == 1:
        returns_clause = f"RETURNS {out_params[0][1]}"
    elif len(out_params) > 1:
        returns_fields = ", ".join(f"{name} {dtype}" for name, dtype in out_params)
        returns_clause = f"RETURNS TABLE({returns_fields})"
    else:
        returns_clause = "RETURNS void"

    body_match = re.search(r'AS\s+(BEGIN.*END;)', oracle_sql, re.IGNORECASE | re.DOTALL)
    if body_match:
        raw_body = body_match.group(1).strip()

        body_lines = raw_body.splitlines()
        formatted_body_lines = []
        for line in body_lines:
            line = line.rstrip()
            formatted_body_lines.append("    " + line)
        body = "\n".join(formatted_body_lines)
    else:
        body = "    BEGIN\n        -- TODO: Add logic\n    END;"

    in_params_str = ", ".join(param_list)
    postgres_function = f"""CREATE OR REPLACE FUNCTION {proc_name}({in_params_str})
{returns_clause}
LANGUAGE plpgsql
AS $$
{body}
$$;
"""

    return postgres_function



