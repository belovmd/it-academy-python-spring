""" Pupils and languages

There are N pupils and M languages. Every pupil studies Mi languages. Find out
which languages are studied by all pupils, which languages are studied
at list by one pupil.

Input data:
1 line: N - pupils amount
rest of lines: Mi - how many languages pupil [i] studies and languages.

Example:
3          - N pupils amount
2          - M1 how many languages the first pupil studies
Russian    - Languages of the first pupil
English
3          - M2 how many languages the second pupil studies
Russian
Belarusian
English
3
Russian
Italian
French

Output data:
Number of languages which every pupil studies
List of these languages.
Number of languages that at least one pupil studies.
List of these languages.
"""


journal = {}
languages = set()
print('Input N - pupils number:')
n = int(input())
for i in range(n):
    print('Input number of languages for pupil #{}:'.format(i + 1))
    m = int(input())
    pupils_languages = set()
    for _ in range(m):
        language = input()
        pupils_languages.add(language)
        languages.add(language)
    journal[i] = pupils_languages

popular_languages = []
non_popular_languages = []

for language in languages:
    is_everybody_knows = True
    is_at_least_one_knows = False
    for lang_list in journal.values():
        if language in lang_list:
            is_at_least_one_knows = True
        else:
            is_everybody_knows = False
    if is_everybody_knows:
        popular_languages.append(language)
    if is_at_least_one_knows:
        non_popular_languages.append(language)

print(len(popular_languages))
for language in popular_languages:
    print(language)
print(len(non_popular_languages))
for language in non_popular_languages:
    print(language)
