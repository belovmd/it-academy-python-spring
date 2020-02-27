"""Ghosts Age

https://py.checkio.org/en/mission/ghosts-age/

Nicola takes a moment to study the ghosts. He is trying to think up a new
method to determine just how old these ghosts are. He knows that their age
is somehow related to their opacity. To measure their opacity Nikola uses a
scale of 10000 units to 0 units, where 10000 is a completely opaque newborn
ghost (0 years old) and 0 is completely transparent ghost (of an unknown age).

After some experimenting, Nikola thinks he has discovered the law of ghostly
opacity. On every birthday, a ghost's opacity is reduced by a number of
units equal to its age when its age is a Fibonacci number (Read about this
here) or increased by 1 if it is not.

For example:
A newborn ghost -- 10000 units of opacity.
1 year -- 10000 - 1 = 9999 (1 is a Fibonacci number).
2 year -- 9999 - 2 = 9997 (2 is a Fibonacci number).
3 year -- 9997 - 3 = 9994 (3 is a Fibonacci number).
4 year -- 9994 + 1 = 9995 (4 is not a Fibonacci number).
5 year -- 9995 - 5 = 9990 (5 is a Fibonacci number).
Help Nicola write a function which will determine the age of a ghost based on
its opacity. You are given opacity measurements as a number ranging from 0
to 10000 inclusively. The ghosts cannot be older than 5000 years as they
simply disappear after such a long time (really!).

"""


def gen_fibonacci_seq(fibonacci_ind):
    """Generate Fibonacci sequence"""
    prev, nxt = 0, 1
    fibonacci_seq = set()
    fibonacci_seq.add(prev)
    while fibonacci_ind > 0:
        prev, nxt = nxt, prev + nxt
        fibonacci_seq.add(prev)
        fibonacci_ind -= 1
    return fibonacci_seq


def ghost_age(opacity):
    """Define ghost age"""
    calc_opacity, age = 10000, 0
    fibonacci_sequence = gen_fibonacci_seq(20)
    while calc_opacity != opacity and age < 5000:
        age += 1
        if age in fibonacci_sequence:
            calc_opacity -= age
        else:
            calc_opacity += 1
    return age


if __name__ == '__main__':
    assert ghost_age(10000) == 0, "Newborn"
    assert ghost_age(9999) == 1, "1 year"
    assert ghost_age(9997) == 2, "2 years"
    assert ghost_age(9994) == 3, "3 years"
    assert ghost_age(9995) == 4, "4 years"
    assert ghost_age(9990) == 5, "5 years"
