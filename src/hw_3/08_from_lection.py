""" Task about pupils and languages"""

# input information:
languages = {'en', 'ru', 'it', 'fr'}

data = [('Vasia', 'en'), ('Katya', 'en'), ('Katya', 'it'), ('Katya', 'fr'),
        ('Serega', 'fr'), ('Serega', 'en'), ('Olya', 'en'), ('Petya', 'en')]

# task solution
total = {x[0]: [] for x in data}
for name, language in data:
    total[name].append(language)
# print(total)

popular_languages = []
non_popular_languages = []

for language in languages:
    is_everybody_knows = True
    is_at_least_one_knows = False
    for lang_list in total.values():
        if language in lang_list:
            is_at_least_one_knows = True
        else:
            is_everybody_knows = False
    if is_everybody_knows:
        popular_languages.append(language)
    if is_at_least_one_knows:
        non_popular_languages.append(language)

print('Everybody knows:', ', '.join(popular_languages))
print('At least one knows:', ', '.join(non_popular_languages))
