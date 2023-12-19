from alphabet import alphabet


def get_key(val):
    for key, value in alphabet.items():
        if val == value:
            return key
    return ""
