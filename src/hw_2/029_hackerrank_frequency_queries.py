""" Frequency queries task

Hackerrank.com
Practice -> Interview Preparation Kit -> Dictionaries and Hashmaps ->
Frequency Queries

You are given  queries. Each query is of the form two integers described below:
1 x: Insert x in your data structure.
2 y: Delete one occurence of y from your data structure, if present.
3 z: Check if any integer is present whose frequency is exactly z.
If yes, print 1 else 0.

The queries are given in the form of a 2-D array queries of size q where
  queries[i][0] contains the operation, and queries[i][1] contains
  the data element.

The main difficult moment for me here are time tests on Hackerrank.
This solution passed all the tests.
"""


from collections import Counter


def frequency_query(queries):
    result = []
    counts = Counter()
    freq = Counter()
    for operation, number in queries:
        if operation == 1:
            freq[counts[number]] -= 1
            counts[number] += 1
            freq[counts[number]] += 1
        if operation == 2:
            if counts[number] > 0:
                freq[counts[number]] -= 1
                counts[number] -= 1
                freq[counts[number]] += 1
        elif operation == 3:
            result.append(1 if freq[number] else 0)
    return result


if __name__ == '__main__':
    # Example
    q = [(3, 4), (2, 100), (1, 16), (3, 1)]
    print(frequency_query(q))

    q = [(1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5),
         (3, 2)]
    assert (frequency_query(q)) == [0, 1], 'Test 1'

    q1 = [(1, 55), (1, 22), (1, 55), (3, 2), (3, 3), (2, 22), (3, 1), (2, 44),
          (2, 55), (3, 1), (3, 2)]
    assert (frequency_query(q1)) == [1, 0, 0, 1, 0], 'Test 2'

    q2 = [(1, 3), (2, 3), (3, 2), (1, 4), (1, 5), (1, 5), (1, 4), (3, 2),
          (2, 4), (3, 2)]
    assert (frequency_query(q2)) == [0, 1, 1], 'Test 3'
