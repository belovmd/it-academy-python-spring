# 15 lines: itertools
from itertools import groupby
lines = """
This is the
first paragraf

This is the second
""".splitlines()
# Use itertools.groupby and bool to return groups
# consecutive lines that either have content or don't.
for has_chars, frags in groupby(lines, bool):
    if has_chars:
        print(' '.join(frags))
# Prints:
# This is the first line
# This is the second.
