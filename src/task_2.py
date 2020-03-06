from datetime import date


def most_frequent_days(a):
    """Days in year counter

    Given a year as an integer (e. g. 2001). You should return the most
    frequent day(s) of the week in that particular year. The result has
    to be a list of days sorted by the order of days in a week
    (e. g. ['Monday', 'Tuesday']). Week starts with Monday.
    :param a: Year as an int
    :return: The list of most common days sorted by the order of days in a
    week (from Monday to Sunday)
    """
    week_days = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }

    start, end = date(a, 1, 1).isoweekday(), date(a, 12, 31).isoweekday()

    popular_days = {}

    day = start

    while True:
        day = 1 if day == 8 else day
        popular_days.update({day: week_days[day]})
        if day == end:
            break
        day += 1
    return [popular_days[day] for day in sorted(popular_days)]


if __name__ == '__main__':
    print("Example:")
    print(most_frequent_days(1084))

    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']
    print("Coding complete? Click 'Check' to earn cool rewards!")
