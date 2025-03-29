def instr_to_position(name_func):
    if "INSTR" in name_func:
        return name_func.replace("INSTR", "POSITION")
    elif "instr" in name_func:
        return name_func.replace("instr", "POSITION")

