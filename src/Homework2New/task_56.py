def checkio(number):
    """Fed pigeons

    I start to feed one of the pigeons. A minute later two more fly by and
    a minute after that another 3. Then 4, and so on (Ex: 1+2+3+4+...). One
    portion of food lasts a pigeon for a minute, but in case there's not
    enough food for all the birds, the pigeons who arrived first ate first.
    Pigeons are hungry animals and eat without knowing when to stop. If I
    have N portions of bird feed, how many pigeons will be fed with at least
    one portion of wheat?
    :param number: integer
    :return: integer
    """
    fed = number
    pigeons = 0
    minute = 1
    while fed > pigeons:
        pigeons += minute
        fed -= pigeons
        minute += 1
    return min(pigeons, pigeons + fed)


if __name__ == '__main__':

    assert checkio(1) == 1
    assert checkio(2) == 1
    assert checkio(5) == 3
    assert checkio(10) == 6
    assert checkio(99999) == 3486
    assert checkio(10000) == 741
