def sun_angle(time):
    """Find the angle of the sun above the horizon knowing the time of the day

    :param time: string format of time '00:00'
    :return: angle value in float format
    """
    if time[:2] < '06' or (time[:2] >= '18' and time[3:] > '00'):
        return "I don't see the sun!"
    return (int(time[:2]) - 6 + int(time[3:]) / 60) * 15


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")