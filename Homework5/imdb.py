# 4 --------------------------------------------------------------------------
# В файле хранятся данные с сайта IMDB.
# Скопированные данные хранятся в файле ./data5/ ratings.list.
# Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.

try:
    f = open("./data5/ratings.list", "r")
except Exception as err:
    print(err)
else:
    top250, ratings, years = [], {}, {}
    while True:
        line = f.readline()
        if not line or line[:3] == "New":
            break
    while True:
        line = f.readline().strip()
        if not line or line[:6] == "BOTTOM":
            break
        lst_line = line.split()
        year = lst_line.pop()[1:5]
        years[year] = years.get(year, 0) + 1
        rating = lst_line[2]
        ratings[rating] = ratings.get(rating, 0) + 1
        top250.append(' '.join(lst_line[3:]))
    f.close()
    with open("./data5/top250_movies.txt", "w") as f:
        for line in top250:
            f.write(line + "\n")
    with open("./data5/ratings.txt", "w") as f:
        ratings = sorted(ratings.items(), key=lambda item: item[1], reverse=True)
        f.write("Rank : Repetition\n")
        for line in ratings:
            str_format = "{:>4} : {:>3} {:*^" + str(line[1]) + "}\n"
            f.write(str_format.format(line[0], line[1], "*"))
    with open("./data5/years.txt", "w") as f:
        years = sorted(years.items(), key=lambda item: item[1], reverse=True)
        for line in years:
            f.write("{} : {}\n".format(line[0], line[1]))
