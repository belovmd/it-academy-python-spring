"""Pawn Brotherhood.

A pawn is generally a weak unit, but we have 8 of them which we can use
to build a pawn defense wall. With this strategy, one pawn defends the
others. A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board and only white pawns.
You should design your code to find how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.
Output: The number of safe pawns as a integer.
Example:
safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

"""


def safe_pawns(pawns: set) -> int:
    hz = 'abcdefgh'
    vt = '12345678'
    s_pawns = 0
    for pos in pawns:
        h_i = hz.index(pos[0])
        v_i = vt.index(pos[1])
        hz_left = hz[h_i - 1] if h_i - 1 >= 0 else ''
        hz_right = hz[h_i + 1] if h_i + 1 <= 7 else ''
        vt_low = vt[v_i - 1] if v_i - 1 >= 0 else ''
        pawn_l = hz_left + vt_low
        pawn_r = hz_right + vt_low
        if pawn_l in pawns or pawn_r in pawns:
            s_pawns += 1
    return s_pawns


if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("DONE!")
