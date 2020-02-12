def checkio(data: str) -> bool:
    """Password secure

    The password will be considered strong enough if its length is
    greater than or equal to 10 symbols, it has at least one digit,
    as well as containing one uppercase letter and one lowercase
    letter in it.
    """

    flag_1, flag_2, flag_3 = False, False, False
    if len(data) >= 10:
        for char in data:
            if '0' <= char <= '9':
                flag_1 = True
            elif 'a' <= char <= 'z':
                flag_2 = True
            elif 'A' <= char <= 'Z':
                flag_3 = True
        return flag_1 == flag_2 == flag_3
    return False
