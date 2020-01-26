def solution(number):
    """Instructions

    Finish the solution so that it returns the sum of all
    the multiples of 3 or 5 below the number passed in.
    """
    sum_num = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            sum_num += num
    return sum_num
    # return sum([num for num in range(number)
    #            if num % 3 == 0 or num % 5 == 0])
    # return sum(filter(
    #    lambda x: x % 3 == 0 or x % 5 == 0, range(number)))


if __name__ == '__main__':
    print(solution(int(input('Enter the number: '))))
