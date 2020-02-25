def task1(s):
    """Task 'Yes-No' from lection

    Print 'Yes' ofter string number if it has appeared in line already, else
    print 'No' after string number
    :param s: string of integers split by whitespaces
    :return: None
    """
    s = ''.join(s.split())
    char_set = set(s)
    for char in s:
        if char in char_set:
            print(f'{char}: No')
            char_set.remove(char)
        else:
            print(f'{char}: Yes')


if __name__ == '__main__':
    task1('1 2 3 2 5 6 1 3')
