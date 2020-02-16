"""Pearls in the Box

To start the game they put several black and white pearls in one of the boxes.
Each robot has N moves, after which the initial set is being restored for the
next game. Each turn, the robot takes a pearl out of the box and puts one of
the opposite color back. The winner is the one who takes the white pearl on
the Nth move. Our robots don't like uncertainty, that's why they want to
know the probability of drawing a white pearl on the Nth move. The probability
is a value between 0 (0% chance or will not happen) and 1 (100% chance or
will happen). The result is a float from 0 to 1 with two decimal digits of
precision (±0.01).

You are given a start set of pearls as a string that contains "b" (black)
and "w" (white) and the number of the move (N). The order of the pearls
does not matter.

"""
from collections import Counter


def probability_white_and_black(marbles: str, step: int) -> float:
    lst = []

    def w_b(marbles, step, m=None):
        m = m if m is not None else 1
        if step == 1:
            return lst.append(m * Counter(marbles)['w'] / len(marbles))
        white_black = Counter(marbles)
        whites = white_black.get('w', 0)
        blacks = white_black.get('b', 0)
        if whites > 0 and blacks > 0:
            take_w = ('w' * (whites - 1)) + ('b' * (blacks + 1))
            take_b = ('w' * (whites + 1)) + ('b' * (blacks - 1))
            m_w = (whites / len(marbles)) * m
            m_b = (blacks / len(marbles)) * m
            w_b(take_w, step - 1, m_w)
            w_b(take_b, step - 1, m_b)
        elif blacks == 0 and whites > 0:
            take_w = ('w' * (whites - 1)) + 'b'
            w_b(take_w, step - 1, m)
        elif whites == 0 and blacks > 0:
            take_b = ('b' * (blacks - 1)) + 'w'
            w_b(take_b, step - 1, m)
        else:
            pass
    w_b(marbles, step)
    return round(sum(lst), 2)


if __name__ == '__main__':
    assert probability_white_and_black('bbw', 3) == 0.48
    assert probability_white_and_black('wwb', 3) == 0.52
    assert probability_white_and_black('www', 3) == 0.56
    assert probability_white_and_black('bbbb', 1) == 0
    assert probability_white_and_black('wwbb', 4) == 0.5
    assert probability_white_and_black('bwbwbwb', 5) == 0.48
    assert probability_white_and_black('wwwwwbwbwbbwbbwwbw', 11) == 0.53
    print("All tests passed!!!")
