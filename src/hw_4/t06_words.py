""" Words

Read a text from input. Text contains words. Word is a chain of
non-whitespace symbols following one by one. Words are separated with one
ore more whitespaces or symbols of the end of line. Find out how many
different words are in the text.
Whitespace symbols: [ \f\n\r\t\v], non-whitespace symbols: all other symbols
except whitespace symbols.
"""

print('Input line numbers:')
n = int(input())
print('Input {} line of text:'.format(n))
text = ''
for _ in range(n):
    text += input() + '\n'

print('There are {} different words.'.format(len(set(text.split()))))
