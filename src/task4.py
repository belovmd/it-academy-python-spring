# В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в
# файле ./data5/ ratings.list.
# a) Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# b) Найдите ТОП250 фильмов и извлеките заголовки.
# c) Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
lst = []
try:
    file = open('ratings.list')
except FileNotFoundError:
    print('File not found.')
else:
    line = file.readlines()
    for i in range(28, 278):
        lst.append(line[i].strip())
    file.close()
file2 = open('top250_movies.txt', 'w')
for i in range(0, 250):
    file2.write(str(i + 1) + '. ' + ' '.join(lst[i].split()[3:]) + '\n')
file2.close()
