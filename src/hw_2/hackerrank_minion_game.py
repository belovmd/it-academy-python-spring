""" https://www.hackerrank.com/challenges/the-minion-game/problem

Kevin and Stuart want to play the 'The Minion Game'.
Game Rules
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.
Input Format
A single line of input containing the string S.
Note: The string S will contain only uppercase letters: [A-Z].

Constraints: 0<len(S)<10**6

Output Format
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.

Example:
    BANANA
    Kevin: B, N, BA, NA, BAN, NAN, NANA, NANA, BANAN, BANANA
          1 + 2 + 1  + 2  +1  +1   +1    +1     +1    +1     = 12
    Stewart: A, AN, ANA, ANAN, ANANA
             3  + 2  +2  + 1   + 1  = 9
"""


def minion_game(s):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    length = len(s)
    for i in range(length):
        if s[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")
    return


if __name__ == '__main__':
    string = input()
    minion_game(string)