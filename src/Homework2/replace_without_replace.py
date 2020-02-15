""" ДЗ с лекции 13-02-20
Заменить все пробелы в строке на точки не используя replace.

"""
string = 'Today it is beautiful bright morning sunrise.'
new_str = '.'.join(string.split())
print(new_str)