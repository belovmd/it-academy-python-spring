BOARD_SIZE = 8


class BailOut(Exception):

    def __init__(self, *args, **kwargs):
        if args:
            self.args = args
            print(args)
        else:
            print(f"Failed to choose the position "
                  f"for the {kwargs['last']} Queen: "
                  f"move right {kwargs['last'] - 1} Queen")

    def not_validate(self):
        if self.args:
            print(f'Not valid schema: '
                  f'Move right Queen number {len(self.args[0])}')


def validate(queens):
    left = right = col = queens[-1]
    for r in reversed(queens[:-1]):
        left, right = left - 1, right + 1
        if r in (left, col, right):
            raise BailOut(queens)


def add_queen(queens):
    for i in range(BOARD_SIZE):
        test_queens = queens + [i]
        try:
            validate(test_queens)
            if len(test_queens) == BOARD_SIZE:
                return test_queens
            else:
                return add_queen(test_queens)
        except BailOut as bo:
            bo.not_validate()
    raise BailOut(last=len(test_queens))


all_queens = add_queen([])
print(all_queens)
print("\n".join(". " * q + "Q " + ". " * (BOARD_SIZE - q - 1)
                for q in all_queens))
