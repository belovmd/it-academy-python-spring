"""Sun Angle.

Your task is to find the angle of the sun above the horizon knowing the time
of the day. Input data: the sun rises in the East at 6:00 AM, which
corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its
zenith, which means that the angle equals 90 degrees. 6:00 PM is the time
of the sunset so the angle is 180 degrees. If the input will be the time of
the night (before 6:00 AM or after 6:00 PM), your function should return -
"I don't see the sun!".

Input: The time of the day.
Output: The angle of the sun, rounded to 2 decimal places.
Example:
sun_angle("07:00") == 15
sun_angle("12:15"] == 93.75
sun_angle("01:23") == "I don't see the sun!"

"""


def sun_angle(time):
    hh, mm = tuple(map(int, time.split(':')))
    now = hh + mm / 60
    if now > 18 or now < 6:
        return "I don't see the sun!"
    return (12 - (18 - now)) * 180 / 12


if __name__ == '__main__':
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Complete!!! All tests passed!!!")
