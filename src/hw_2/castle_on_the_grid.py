""" Castle on the grid

Hackerranc.com -> Practice -> Interview Preparation Kit -> Stacks and Queues
-> Castle on the grid

You are given a square grid with some cells open (.) and some blocked (X).
Your playing piece can move along any row or column until it reaches the edge
of the grid or a blocked cell. Given a grid, a start and an end position,
determine the number of moves it will take to get to the end position.

For example, you are given a grid with sides n = 3 described as follows:
    . . .
    . x .
    . . .
Your starting position (0, 0) so you start in the top left corner. The ending
position is (1, 2). The path is (0, 0) -> (0, 2) -> (1, 2).
It takes 2 moves to get to the goal.
Complete the minimumMoves function in the editor. It must print an integer
denoting the minimum moves required to get from the starting position to the
goal."""

from collections import deque
from collections import namedtuple


def append_cell(cell, cell_to_move, q, visited, moves):
    if cell_to_move not in visited:
        q.append(cell_to_move)
        visited.add(cell_to_move)
        moves[cell_to_move] = moves[cell] + 1
    return


def print_moves(moves, n):
    # print(moves)
    m = []
    for i in range(n):
        m.append([0 for _ in range(n)])
    for c in moves:
        m[c.x][c.y] = moves[c]
    for i in range(n):
        print(m[i])
    return


def bfs(allowed, start_position, finish_position):
    """
    Returns the number of steps(rotations) needs to go to finish

    Some notes:
    Pay attention that according to the task description 'moves' means
    'rotations'.
    """

    # Cells for visiting (queue).
    q = deque()
    Cell = namedtuple('Cell', ['x', 'y'])
    start = Cell(start_position[0], start_position[1])
    q.append(start)

    # Cells that were visited already.
    visited = set()
    visited.add(start)

    # moves[i] - number of rotations need to be done in order to get
    # from start cell to i-cell.
    moves = {start: 0}

    while len(q):
        cell = q.popleft()

        # north
        x = cell.x - 1
        while x >= 0:
            if allowed[x][cell.y]:
                cell_to_move = Cell(x, cell.y)
                append_cell(cell, cell_to_move, q, visited, moves)
                x -= 1
            else:
                break
        # east
        y = cell.y + 1
        while y < len(allowed):
            if allowed[cell.x][y]:
                cell_to_move = Cell(cell.x, y)
                append_cell(cell, cell_to_move, q, visited, moves)
                y += 1
            else:
                break
        # south
        x = cell.x + 1
        while x < len(allowed):
            if allowed[x][cell.y]:
                cell_to_move = Cell(x, cell.y)
                append_cell(cell, cell_to_move, q, visited, moves)
                x += 1
            else:
                break
        # west
        y = cell.y - 1
        while y >= 0:
            if allowed[cell.x][y]:
                cell_to_move = Cell(cell.x, y)
                append_cell(cell, cell_to_move, q, visited, moves)
                y -= 1
            else:
                break
    # print_moves(moves, len(allowed))
    return moves[finish_position]


def minimum_moves(grid, start_x, start_y, goal_x, goal_y):
    size = len(grid)
    allowed = []
    for x in range(0, size):
        tmp = [1 if grid[x][y] == '.' else 0 for y in range(size)]
        allowed.append(tmp)
    return bfs(allowed, (start_x, start_y), (goal_x, goal_y))


if __name__ == '__main__':
    grid1 = ['...',
             '.x.',
             '...']
    start_x1 = 0
    start_y1 = 0
    goal_x1 = 1
    goal_y1 = 2
    assert(minimum_moves(grid1, start_x1, start_y1,
                         goal_x1, goal_y1)) == 2, 'Test 1'

    grid2 = ['...x...',
             '.x.x...',
             '....x..',
             'x...x..',
             '....x..',
             '.......',
             '...x...']
    assert (minimum_moves(grid2, 0, 0, 1, 4)) == 5, 'Test 2'
    assert(minimum_moves(grid2, 1, 4, 0, 0)) == 5, 'Test 3'

    # example:
    # print(minimum_moves(grid2, 1, 4, 0, 0))
