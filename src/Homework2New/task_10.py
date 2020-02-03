def dirReduc(arr):
    """Instructions

    In ["NORTH", "SOUTH", "EAST", "WEST"], the
    direction "NORTH" + "SOUTH" is going north
    and coming back right away.
    The path becomes ["EAST", "WEST"], now "EAST"
    and "WEST" annihilate each other, therefore,
    the final result is [] (nil in Clojure).
    In ["NORTH", "EAST", "WEST", "SOUTH", "WEST",
    "WEST"], "NORTH" and "SOUTH" are not directly
    opposite but they become directly opposite after
    the reduction of "EAST" and "WEST" so the whole
    path is reducible to ["WEST", "WEST"].
    """
    dict_dir = {'NORTH': 1, 'WEST': 2, 'SOUTH': -1, 'EAST': -2}
    test_dir = []
    for index in range(len(arr)):
        if not test_dir or dict_dir[arr[index]] + \
                dict_dir[test_dir[-1]] != 0:
            test_dir.append(arr[index])
        else:
            test_dir.pop()
    return test_dir


if __name__ == '__main__':
    list_of_dir = ["NORTH", "SOUTH", "SOUTH",
                   "EAST", "WEST", "NORTH", "WEST"]
    print(dirReduc(list_of_dir))
