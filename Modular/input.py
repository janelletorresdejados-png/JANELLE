def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None


def read_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        return None