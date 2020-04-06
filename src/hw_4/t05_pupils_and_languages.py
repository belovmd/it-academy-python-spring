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
# languages = set()

with open('t05_input.txt', 'r') as file:
    pupils_count = int(file.readline())
    for i in range(pupils_count):
        languages_count = int(file.readline())
        pupils_languages = set()
        for _ in range(languages_count):
            pupils_languages.add(file.readline().strip())
        journal[i] = pupils_languages

popular_languages = set.intersection(*journal.values())
non_popular_languages = set.union(*journal.values())

print(len(popular_languages))
for language in popular_languages:
    print(language)
print(len(non_popular_languages))
for language in non_popular_languages:
    print(language)
