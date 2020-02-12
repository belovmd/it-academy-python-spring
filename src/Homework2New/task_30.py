def time_converter(time):
    """Time formatter

    :param time: string format of time '00:00'
    :return: string format of time '12:00 a.m.'
    """
    if time[:2] == '00':
        return '12' + time[2:] + ' a.m.'
    elif time[:2] < '12':
        return time[1:] + ' a.m.' if time[:2] < '10' else time + ' a.m.'
    return time + ' p.m.' if time[:2] == '12' \
        else str(int(time[:2]) - 12) + time[2:] + ' p.m.'


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('00:15') == '12:15 a.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
