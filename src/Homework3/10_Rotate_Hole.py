"""Rotate Hole

The loading automaton has a program with the pipe numbers which indicate
where it should place cannonballs. These numbers cannot be changed as they
are engraved into the pipes. We can, however, rotate the backend mechanism
to change the correspondence between pipes and cannons. We should find each
combination that we can rotate the backend mechanism so that all loaded
cannonballs will be loaded into the still-working cannons. The loading
automaton will load all of the balls simultaneously.

The pipes are numbered from 0 to N-1. The initial positions of the backend
mechanism are represented as an array with 1 and/or 0. Each element describes
a cannon behind the pipe; the 0th element describe 0th pipe. 1 is a working
cannon and 0 is a broken cannon.

You know the pipe numbers where the automaton will load cannonballs
(sometimes it loads several cannonballs into one cannon). Your goal is
to find all the combinations that you can rotate the backend mechanism in
a clockwise manner so that all of the cannonballs will be loaded into the
working cannons. Rotation is described as an integer - how many units you
should rotate clockwise. The result should be represented as a list of
integers (variants) in the ascending order. The case when you don't need
to rotate are described as 0 (but don't forget about other variants).
If it's not possible to find a solution, then return [].

For example, the initial state is [1,0,0,0,1,1,0,1,0,0,0,1]
and pipes numbers are [0,1]. If you rotate the mechanism by 1 or 8 units,
then all balls which are be placed in the 0th and 1st pipes will be in cannons.

"""


def rotate(state, pipe_numbers):
    def one_step_rotation(state):
        tmp = state[-1]
        for ind in range(len(state) - 1, 0, -1):
            state[ind] = state[ind - 1]
        state[0] = tmp
        return state

    def check_state(state):
        for ind in pipe_numbers:
            if state[ind] != 1:
                return False
        return True
    state_cnt = list()
    if check_state(state):
        state_cnt.append(0)
    for step in range(1, len(state)):
        if check_state(one_step_rotation(state)):
            state_cnt.append(step)
    return state_cnt


if __name__ == '__main__':
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8]
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == []
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0]
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5]
    assert rotate(
        [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1,
         0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1,
         1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1,
         0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1,
         0, 0, 0, 1, 1, 1, 0, 0],
        [17, 43, 34, 89, 28, 54]) == [21, 84]
    print('All tests passed!!!')
