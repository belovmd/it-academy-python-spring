# Пары элементов
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
pair_list = [1, 1, 1]
pairs = 0
for i in range(len(pair_list)):
    for j in range(i + 1, len(pair_list)):
        if pair_list[i] == pair_list[j]:
            pairs += 1
print(pairs)
