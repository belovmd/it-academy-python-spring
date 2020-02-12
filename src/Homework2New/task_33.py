def long_repeat(line: str) -> int:
    """length the longest substring that consists of the same char"""
    count = result = 0

    for i in range(len(line)):

        for j in range(i, len(line)):

            if line[i] == line[j]:
                count += 1
            else:
                break

        if count > result:
            result = count

        count = 0

    return result


if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
