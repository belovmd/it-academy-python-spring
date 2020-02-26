"""Cipher Map

https://py.checkio.org/en/mission/cipher-map2/

Help Sofia write a decrypter for the passwords that Nikola will encrypt
through the cipher map. A cipher grille is a 4×4 square of paper with four
windows cut out. Placing the grille on a paper sheet of the same size, the
encoder writes down the first four symbols of his password inside the windows
(see fig. below). After that, the encoder turns the grille 90 degrees
clockwise. The symbols written earlier become hidden under the grille and
clean paper appears inside the windows. The encoder then writes down the
next four symbols of the password in the windows and turns the grille 90
degrees again. Then, they write down the following four symbols and turns
the grille once more. Lastly, they write down the final four symbols of the
password. Without the same cipher grille, it is difficult to discern the
password from the resulting square comprised of 16 symbols. Thus, the encoder
can be confident that no hooligan will easily gain access to the locked door.

"""


def rotate_grille(cip_gr):
    """Turn the grille 90 degrees clockwise"""
    row, col = len(cip_gr), len(cip_gr[0])
    return [[cip_gr[r_i][c_i] for r_i in (
        range(row - 1, -1, -1))] for c_i in range(col)]


def convert_grille_to_list(cipher_grille):
    """Convert cipher_grille to changing data structure - list"""
    return [[1 if col == 'X' else 0 for col in row] for row in cipher_grille]


def get_symbols(cip_gr, cip_pass):
    """Get symbols from cip_pass by cip_gr pattern"""
    return ''.join(
        [cip_pass[r_i][c_i] for r_i in range(4) for c_i in (
            range(4)) if cip_gr[r_i][c_i] == 1])


def recall_password(cipher_grille, ciphered_password):
    """Password decrypter"""
    cipher_grille = convert_grille_to_list(cipher_grille)
    decode_lst = list()
    for _ in range(4):
        decode_lst.append(get_symbols(cipher_grille, ciphered_password))
        cipher_grille = rotate_grille(cipher_grille)
    return ''.join(decode_lst)


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
