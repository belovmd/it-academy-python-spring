"""Каждый из N школьников некоторой школы знает Mi языков.

Определите, какие языки знают все школьники и языки,

которые знает хотя бы один из школьников.

"""

union = set()
pupils = set()
for quantity_pupils in range(int(input("Enter quantity puplis: "))):
    language = {input("Enter language: ") for element in
                range(int(input("Enter quantity languages: ")))}
    pupils.update(language)
    if quantity_pupils == 1:
        union.update(language)
    else:
        union &= language
print(len(union))
print('\n'.join(sorted(union)))
print(len(pupils))
print('\n'.join(sorted(pupils)))
