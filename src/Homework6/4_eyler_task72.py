"""4 - Проект Эйлера (Variant 13: task 72)

Задача 72 - Счет дробей

Рассмотрим дробь n/d, где n и d являются положительными целыми числами.
Если n<d и НОД(n,d) = 1, то речь идет о сокращенной правильной дроби.
Если перечислить множество сокращенных правильных дробей для d ≤ 8 в порядке
возрастания их значений, получим:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
5/7, 3/4, 4/5, 5/6, 6/7, 7/8

Нетрудно заметить, что данное множество состоит из 21 элемента.
Из скольки элементов будет состоять множество сокращенных правильных дробей
для d ≤ 1 000 000?

"""
import math
from operator import mul
from functools import reduce


def fraction_counter_slowly(number: int) -> list:
    """Return count of reduced fractions"""
    fractions = []
    for n in range(1, number):
        for d in range(number, 0, -1):
            if n < d:
                if math.gcd(n, d) == 1:
                    fractions.append((n, d))
            else:
                break
    return len(fractions)


def prime_factors(n):
    res = set()
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.add(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n+1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.add(i)
            n //= i
            limit = math.sqrt(n+i)
        else:
            i += 2
    if n != 1:
        res.add(n)
    return res

def totient(n):
    if n == 1: return 1
    return int(round(n * reduce(mul, [1 - 1.0 / p for p in prime_factors(n)])))

def farey_length(n):
    return sum(totient(m) for m in range(1, n+1)) - 1

def main():
    print(farey_length(1000000))

if __name__ == "__main__": main()