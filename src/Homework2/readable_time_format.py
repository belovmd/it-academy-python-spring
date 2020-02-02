"""Make human-readable time format.

Write a function, which takes a non-negative integer (seconds) as input
and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

"""
import unittest


def seconds_to_time_format(seconds):
    """Return string in human-readable time format."""
    hh = mm = 0
    if seconds > 359999:
        raise ValueError

    if seconds >= 3600:
        hh = seconds // 3600
        seconds -= hh * 3600

    if seconds >= 60:
        mm = seconds // 60
        seconds -= mm * 60

    return f'{hh:02d}:{mm:02d}:{seconds:02d}'


class TestTimeConvert(unittest.TestCase):
    def test_time_convert(self):
        self.assertEqual(seconds_to_time_format(0), "00:00:00")
        self.assertEqual(seconds_to_time_format(5), "00:00:05")
        self.assertEqual(seconds_to_time_format(60), "00:01:00")
        self.assertEqual(seconds_to_time_format(86399), "23:59:59")
        self.assertEqual(seconds_to_time_format(359999), "99:59:59")


if __name__ == '__main__':
    unittest.main()
