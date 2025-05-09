import re

def to_interval(sql):

    def convert_dsinterval(match):
        value = match.group(1).strip()
        value_parts = value.split()

        if len(value_parts) == 2:
            days = int(value_parts[0])
            time_part = value_parts[1]
            return f"INTERVAL '{days} days {time_part}'"
        elif ':' in value:
            return f"INTERVAL '0 days {value}'"
        else:
            return f"INTERVAL '{int(value)} days'"

    def convert_yminterval(match):
        value = match.group(1).strip()
        years, months = 0, 0

        if '-' in value:
            y, m = value.split('-')
            years = int(y)
            months = int(m)
        else:
            years = int(value)

        parts = []
        if years:
            parts.append(f"{years} years")
        if months:
            parts.append(f"{months} months")
        if not parts:
            parts.append("0 months")

        return f"INTERVAL '{' '.join(parts)}'"

    sql = re.sub(r"TO_DSINTERVAL\s*\(\s*'([^']+)'\s*\)", convert_dsinterval, sql, flags=re.IGNORECASE)
    sql = re.sub(r"TO_YMINTERVAL\s*\(\s*'([^']+)'\s*\)", convert_yminterval, sql, flags=re.IGNORECASE)

    return sql
