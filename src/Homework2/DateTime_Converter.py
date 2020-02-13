"""Date and Time Converter.

Computer date and time format consists only of numbers, for example:
21.05.2018 16:30. Humans prefer to see something like this: 21 May 2018
year, 16 hours 30 minutes. Your task is simple - convert the input date and
time from computer format into a "human" format.

"""
import unittest


def date_time(date_time: str) -> str:
    month_d = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }
    date, time = date_time.split()
    d, m, y = date.split('.')
    h, mm = time.split(':')
    h_w = 'hour' if int(h) == 1 else 'hours'
    m_w = 'minute' if int(mm) == 1 else 'minutes'
    return f'{int(d)} {month_d[m]} {y} year {int(h)} {h_w} {int(mm)} {m_w}'


class TestDateConverter(unittest.TestCase):
    def test_data_converter(self):
        result_lst = [
            "1 January 2000 year 0 hours 0 minutes",
            "9 May 1945 year 6 hours 30 minutes",
            "20 November 1990 year 3 hours 55 minutes",
        ]
        self.assertEqual(date_time("01.01.2000 00:00"), result_lst[0])
        self.assertEqual(date_time("09.05.1945 06:30"), result_lst[1])
        self.assertEqual(date_time("20.11.1990 03:55"), result_lst[2])


if __name__ == '__main__':
    unittest.main()
