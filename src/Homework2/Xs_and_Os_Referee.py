"""Xs and Os Referee.

You are given a result of a game and you must determine if the game ends in
a win or a draw as well as who will be the winner. Make sure to return "X"
if the X-player wins and "O" if the O-player wins. If the game is a draw,
return "D". A game's result is presented as a list of strings, where "X"
and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).
Output: "X", "O" or "D" as a string.
Example:
checkio(["X.O", "XX.", "XOO"]) == "X"
checkio(["OO.", "XOX", "XOX"]) == "O"
checkio(["OOX", "XXO", "OXX"]) == "D"

"""
from typing import List


def checkio(game_res: List[str]) -> str:
    for i in range(3):
        if game_res[0][i] == game_res[1][i] == game_res[2][i] != '.':
            return game_res[0][i]
        elif game_res[i][0] == game_res[i][1] == game_res[i][2] != '.':
            return game_res[i][0]
    if game_res[0][0] == game_res[1][1] == game_res[2][2] != '.':
        return game_res[0][0]
    elif game_res[0][2] == game_res[1][1] == game_res[2][0] != '.':
        return game_res[0][2]
    else:
        return 'D'


if __name__ == '__main_@_':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print('DONE!!!')
