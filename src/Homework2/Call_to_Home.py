"""Call to Home

The bill is represented as an array with information about the calls. Help
Nicola to calculate the cost for each of Sophia calls. Each call is
represented as a string with date, time and duration of the call in seconds
in the follow format: "YYYY-MM-DD hh:mm:ss duration"
The date and time in this information are the start of the call.
Space-Time Communications Co. has several rules on how to calculate the cost
of calls:

First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
After 100 minutes in one day, each minute costs 2 coins per minute;
All calls are rounded up to the nearest minute. For example 59 sec ≈ 1 min,
61 sec ≈ 2 min;
Calls count on the day when they began. For example if a call was started
2014-01-01 23:59:59, then it counted to 2014-01-01;

For example:

2014-01-01 01:12:13 181
2014-01-02 20:11:10 600
2014-01-03 01:12:13 6009
2014-01-03 12:13:55 200

First day -- 181s≈4m -- 4 coins;
Second day -- 600s=10m -- 10 coins;
Third day -- 6009s≈101m + 200s≈4m -- 100 + 5 * 2 = 110 coins;
Total -- 124 coins.

"""


def total_cost(calls):
    day_calls = dict()
    for call in calls:
        day, _, sec = call.split()
        minutes = int(sec) // 60 if int(sec) % 60 == 0 else int(sec) // 60 + 1
        day_calls[day] = day_calls.get(day, 0) + minutes
    amount_coast = 0
    for data, minutes in day_calls.items():
        if minutes < 100:
            amount_coast += minutes * 1
        else:
            amount_coast += 100 + (minutes - 100) * 2
    return amount_coast


if __name__ == '__main__':
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106
    print('All tests passed!!!')
