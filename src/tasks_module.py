def swap_numbers(number_list: list):
    for element in number_list:
        if element == 0:
            number_list.remove(element)
            number_list.append(element)
    print(number_list)


def fibonacci(number: int):
    first__elem = 1
    second_elem = 1
    fibonacci_list = []
    if first__elem == 1:
        fibonacci_list.append(1)
    if second_elem == 1:
        fibonacci_list.append(1)
    for i in range(number):
        first__elem, second_elem = second_elem, first__elem + second_elem
        fibonacci_list.append(second_elem)
    print(fibonacci_list)


def remove_duplicate_characters(words: str):
    word = str()
    for element in words:
        if element not in word:
            word += element
    print(word.replace(" ", ""))
