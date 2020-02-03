"""Dice Game.

Greed is a dice game played with five six-sided dice.
Your mission, should you choose to accept it, is to score
a throw according to these rules. You will always be given
an array with five six-sided dice values.

Three 1's => 1000 points
Three 6's =>  600 points
Three 5's =>  500 points
Three 4's =>  400 points
Three 3's =>  300 points
Three 2's =>  200 points
One   1   =>  100 points
One   5   =>   50 point

A single die can only be counted once in each roll. For example,
a "5" can only count as part of a triplet (contributing to the 500 points)
or as a single 50 points, but not both in the same roll.

Example scoring

Throw       Score
---------   ------------------
5 1 3 4 1   50 + 2 * 100 = 250
1 1 1 3 1   1000 + 100 = 1100
2 4 4 5 4   400 + 50 = 450

"""
from collections import Counter


def score(dice):
    """Return sum points of dice game."""
    print(dice)
    dice_count = Counter(dice)
    score = {
        111: 1000,
        666: 600,
        555: 500,
        444: 400,
        333: 300,
        222: 200,
        1: 100,
        5: 50,
    }
    sum_score = 0
    for k, v in dice_count.items():
        if v < 3:
            sum_score += score.get(k, 0) * v
        else:
            sum_score += score.get(k * 111, 0) + score.get(k, 0) * (v - 3)
    print(sum_score)
    return sum_score


assert score([5, 1, 3, 4, 1]) == 250
assert score([1, 1, 1, 3, 1]) == 1100
assert score([2, 4, 4, 5, 4]) == 450
