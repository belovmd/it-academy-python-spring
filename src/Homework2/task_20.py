def checker(i, j, field):
    """Checker of boat position"""
    boat = 1

    # checker around first position of a boat
    if field[i + 1][j - 1] or field[i][j + 1] * field[i + 1][j]:
        return 0

    # boat checker in vertical position if boat vertical
    if not field[i][j + 1]:
        while field[i][j] and i <= 9:
            if boat > 4 or field[i + 1][j + 1]:
                return 0
            boat += 1
            field[i][j] = 0
            i += 1
        return boat - 1

    # boat checker in horizontal position if boat horizontal
    if not field[i + 1][j]:
        while field[i][j] and j <= 10:
            if boat > 4 or field[i + 1][j + 1]:
                return 0
            boat += 1
            field[i][j] = 0
            j += 1
        return boat - 1


def validate_battlefield(field):
    """Instructions

    Validator or right position of boat
    in "Sea battle" game
    """
    for i in range(10):
        field[i].insert(0, 0)
        field[i].append(0)
    field.append([0] * 12)
    counter_boats = {1: 4, 2: 3, 3: 2, 4: 1}

    for i in range(10):
        for j in range(1, 11):
            if field[i][j] == 1:
                valid_boat = checker(i, j, field)
                if valid_boat:
                    counter_boats[valid_boat] -= 1
                else:
                    return False

    for boats in counter_boats.values():
        if boats:
            return False
    return True


if __name__ == '__main__':
    battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert validate_battlefield(battleField)
