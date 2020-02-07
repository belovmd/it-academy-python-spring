"""
Your task is to convert the time from the 24-h format into 12-h format
by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday)
or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it.
For example: '9:05 a.m.'

time_converter('12:30') == '12:30 p.m.'
time_converter('09:00') == '9:00 a.m.'
time_converter('23:15') == '11:15 p.m.'

"""


def time_converter(time):
    h, m = time.split(':')
    if int(h) == 12:
        return f'{str(int(h))}:{m} p.m.'
    elif int(h) == 0:
        return f'{str(12)}:{m} a.m.'
    elif int(h) > 12:
        return f'{str(int(h) - 12)}:{m} p.m.'
    else:
        return f'{str(int(h))}:{m} a.m.'


if __name__ == '__main__':
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
