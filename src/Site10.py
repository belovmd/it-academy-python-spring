# 10) A cipher grille is a 4×4 square of paper with four windows cut out.
# Placing the grille on a paper sheet of the same size, the encoder writes down
# the first four symbols of his password inside the windows (see fig. below).
# After that, the encoder turns the grille 90 degrees clockwise. The symbols
# written earlier become hidden under the grille and clean paper appears inside
# the windows. The encoder then writes down the next four symbols of the
# password in the windows and turns the grille 90 degrees again. Then, they
# write down the following four symbols and turns the grille once more. Lastly,
# they write down the final four symbols of the password. Without the same
# cipher grille, it is difficult to discern the password from the resulting
# square  comprised of 16 symbols. Thus, the encoder can be confident that no
# hooligan will easily gain access to the locked door.


def recall_password(cipher_grille, ciphered_password):
    def rotation(mat):
        return [[mat[i][k] for i in range(3, -1, -1)] for k in range(4)]

    cipher_grille = [list(cipher_grille[i]) for i in range(4)]
    ciphered_password = [list(ciphered_password[i]) for i in range(4)]

    letters = ''
    for times in range(4):
        for i in range(4):
            for j in range(4):
                if cipher_grille[i][j] == 'X':
                    letters += ciphered_password[i][j]
        cipher_grille = rotation(cipher_grille)
    return letters


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
