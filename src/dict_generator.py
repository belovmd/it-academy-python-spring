def dict_generator():
    """Dictionary generator

    :return:simple dictionary where
            keys:
                integers from 1 to 20
            values:
                 cubes of integer keys
    """
    return {i: i**3 for i in range(1, 21)}


if __name__ == '__main__':
    print(dict_generator())
