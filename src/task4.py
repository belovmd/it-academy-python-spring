# В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в
# файле ./data5/ ratings.list.
# a) Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# b) Найдите ТОП250 фильмов и извлеките заголовки.
# c) Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
try:
    with open('ratings.list') as file:
        file.read()
except FileNotFoundError:
    print('File not found')
else:
    with open('ratings.list') as file:
        lines = file.readlines()[28:278]
    top_250 = ["{rating} {title} {year}".format(rating=el.split()[2],
                                                title=' '.join(
                                                    el.split()[3: -1]),
                                                year=el.split()[-1]) for el in
               lines]
    with open('top250_movies.txt', 'w') as file:
        for el in top_250:
            file.write(el + '\n')

    years_list = [el.split()[-1].strip('()') for el in lines]
    years_dict = {}
    for el in years_list:
        years_dict[el] = years_dict.get(el, 0) + 1
    with open('years.txt', 'w') as file:
        for year in years_dict:
            file.write(year + ':' + '!' * years_dict[year] + '\n')

    rating_list = [el.split()[2] for el in lines]
    rating_dict = {}
    for el in rating_list:
        rating_dict[el] = rating_dict.get(el, 0) + 1
    with open('rating.txt', 'w') as file:
        for year in rating_dict:
            file.write(year + ':' + '!' * rating_dict[year] + '\n')
