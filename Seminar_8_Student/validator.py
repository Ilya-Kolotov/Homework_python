def is_num(str):
    try:
        int(str)
        return True
    except ValueError:
        return False