"""Sherlock and anagrams

hackerrank.com
Practice -> Interview Preparation Kit -> Dictionaries and Hashmaps ->
    Sherlock and Anagrams

Two strings are anagrams of each other if the letters of one string can be
rearranged to form the other string. Given a string, find the number of pairs
of substrings of the string that are anagrams of each other.

For example s='mom', the list of all anagrammatic pairs is: [m, m], [mo, om]
at positions [[0],[2]], [[0, 1],[1, 2]] respectively. Also see examples below
in a code

Function Description
Complete the function sherlockAndAnagrams in the editor below. It must return
an integer that represents the number of anagrammatic pairs of substrings in s.
"""

from collections import Counter


def sherlock_and_anagrams(s):
    anagram_count = 0
    n = len(s)
    for anagram_length in range(1, n + 1):
        substrings = [''.join(sorted(s[i: i + anagram_length]))
                      for i in range(0, n - anagram_length + 1)]

        s_counter = Counter(substrings)

        for substring, count in s_counter.items():
            if count > 1:
                anagram_count += count * (count - 1) // 2  # C(n, 2)
    return anagram_count


if __name__ == '__main__':
    #  Very good example!.
    s1 = 'ifailuhkqq'
    print(sherlock_and_anagrams(s1))

    assert(sherlock_and_anagrams(s1)) == 3, (
        'Test 1: anagrams are [i, i], [q, q], [ifa, fai]')

    s2 = 'kkkk'
    assert(sherlock_and_anagrams(s2)) == 10, 'Test 2.'
    # k:4, kk:3, kkk:2 ->
    # C(4,2) + C(3,2) + C(2,2) = [n * (n- 1) // 2] =
    # = 4*3/2 + 3*2/2 + 2*1/2 = 6 + 3 + 1 = 10

    s3 = 'cdcd'
    assert (sherlock_and_anagrams(s3)) == 5, (
        'Test 3: [c, c], [d, d], [cd, dc], [cd, cd], [dc, cd]')
