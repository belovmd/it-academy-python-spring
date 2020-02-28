"""Dict comprehension

Написать генератор словарей, который для введенного числа n ставит в
соответствие его текстовой записи квадрат этого числа.

"""
cnt = input('Enter count items in dict:')
entered_numbers = [input(f'Enter number {ind}:') for ind in range(int(cnt))]
dct = {n: int(n) ** 2 for n in entered_numbers}
print(dct)
