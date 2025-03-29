
def to_number_to_cast(name_func):
    name_func.replace('"', "'")
    if "TO_NUMBER" in name_func:
        name_func=name_func.replace("TO_NUMBER", "CAST")
        return name_func.replace("')", "' AS numeric)")
    elif "to_number" in name_func:
        name_func = name_func.replace("to_number", "CAST")
        return name_func.replace("')", "' AS numeric)")

