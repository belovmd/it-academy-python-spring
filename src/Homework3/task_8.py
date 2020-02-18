def recall_password(cipher_grille, ciphered_password):
    """Decrypter for the passwords

    Decrypter for the passwords will encrypt through the cipher map.
    A cipher grille is a 4×4 square of paper with four windows
    cut out. Placing the grille on a paper sheet of the same size, the encoder
    writes down the first four symbols of his password inside the windows
    (see fig. below). After that, the encoder turns the grille 90 degrees
    clockwise. The symbols written earlier become hidden under the grille and
    clean paper appears inside the windows. The encoder then writes down the
    next four symbols of the password in the windows and turns the grille 90
    degrees again. Then, they write down the following four symbols and turns
    the grille once more. Lastly, they write down the final four symbols of
    the password.
    :param cipher_grille: tuple of string
    :param ciphered_password: tuple of string
    :return: string
    """

    second_tuple = tuple(zip(*reversed(cipher_grille)))
    third_tuple = tuple(zip(*reversed(second_tuple)))
    fourth_tuple = tuple(zip(*reversed(third_tuple)))

    cipher_grille_list = [
        cipher_grille,
        second_tuple,
        third_tuple,
        fourth_tuple,
    ]
    password = ''
    for temp_tuple in cipher_grille_list:
        for line_num, line in enumerate(temp_tuple):
            for index, char in enumerate(line):
                if char == 'X':
                    password += ciphered_password[line_num][index]
    return password


if __name__ == '__main__':

    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
