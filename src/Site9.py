# 9) The pipes are numbered from 0 to N-1. The initial positions of the backend
# mechanism are represented as an array with 1 and/or 0. Each element describes
# a cannon behind the pipe; the 0th element describe 0th pipe. 1 is a working
# cannon and 0 is a broken cannon.
# For example, the initial state is [1,0,0,0,1,1,0,1,0,0,0,1] and pipes numbers
# are [0,1]. If you rotate the mechanism by 1 or 8 units, then all balls which
# are be placed in the 0th and 1st pipes will be in cannons.


def rotate(state, pipe_numbers):
    a = [[el + i for el in pipe_numbers] for i in range(0, -len(state), -1)]
    answer = []
    for j in range(len(state)):
        if [state[el] for el in a[j]] == [1] * len(pipe_numbers):
            answer.append(j)
    return answer


if __name__ == '__main__':
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], \
        "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], \
        "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], \
        "Two cannonballs in the same pipe"
