def safe_pawns(pawns: set) -> int:
    """Safe pawns

    A pawn is safe if another pawn can capture a unit on that square
    :param pawns: Placed pawns coordinates as a set of strings
    :return: The number of safe pawns as a integer
    """
    letter_converter = {'a': 1,
                        'b': 2,
                        'c': 3,
                        'd': 4,
                        'e': 5,
                        'f': 6,
                        'g': 7,
                        'h': 8}

    converted_board = [[letter_converter[element[0]],
                        int(element[-1])] for element in pawns]

    counter = 0
    for checking_pawn in converted_board:
        for pawn in converted_board:
            if checking_pawn[1] == pawn[1] + 1 and \
                    (checking_pawn[0] == pawn[0] + 1 or \
                     checking_pawn[0] == pawn[0] - 1):
                counter += 1
                break
    return counter


if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
