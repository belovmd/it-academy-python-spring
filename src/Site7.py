# 7) You are given a set of square coordinates where we have placed white
# pawns. You should count how many pawns are safe.  A pawn is safe if another
# pawn can capture a unit on that square. We have several white pawns on the
# chess board and only white pawns. You should design your code to find how
# many pawns are safe.


def safe_pawns(pawns: set) -> int:
    pawns = list(pawns)
    columns = 'abcdefgh '
    safe = 0

    for el in pawns:
        proverka1 = columns[columns.find(el[0]) - 1] + str(int(el[1]) - 1)
        proverka2 = columns[columns.find(el[0]) + 1] + str(int(el[1]) - 1)
        if proverka1 in pawns or proverka2 in pawns:
            safe += 1
    return safe


if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool "
          "rewards!")
