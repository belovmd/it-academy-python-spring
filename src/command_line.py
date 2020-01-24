# This adds up integers that have been passed as arguments in the command line
import sys
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print(f'sum={total}')
except ValueError:
    print('Please supply integer arguments')
