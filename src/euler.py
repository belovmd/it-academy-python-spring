# 4 --------------------------------------------------------------------------
# 472  https://euler.jakumo.org/problems/view/472.html
# N сидений расположено в ряд. N человек приходят один за другим
# и занимают места в соответствии со следующими правилами:
#
# 1. Никто не садится рядом с кем-то другим.
# 2. Первый человек выбирает любое сидение.
# 3. Каждый следующий человек выбирает дальнейшее сидение от всех уже сидящих,
#  в то же время не нарушая правило номер 1. Если есть несколько возможностей,
#  удовлетворяющих этому условию, человек выбирает сидение,
#  расположенное левее всего.
# Заметим, что из-за первого правила обязательно останутся незанятые сиденья,
# а максимальное число рассевшихся человек будет меньше N (для N > 1).
#
# Пусть f(N) будет количеством выбранных первым человеком сидений,
# которые приведут к максимальному количеству сидящих людей
# в ряду из N сидений.
# Таким образом, f(1) = 1, f(15) = 9, f(20) = 6 и f(500) = 16.
# Также, ∑f(N) = 83 для 1 ≤ N ≤ 20 и ∑f(N) = 13343 для 1 ≤ N ≤ 500.


def euler(N):
    """find  sum(f(N)) for 1 <= n <= N"""
    sum = 0
    for n in range(1, N + 1):
        # How many persons in the maximum rows
        max_persons = []
        # begin from first person
        for first_seat in range(n):
            row = [0 for _ in range(n)]
            person = 1
            row[first_seat] = person
            # fill all other seats while have a free place
            while True:
                weight_seats = [0 for _ in range(n)]
                # count min distances for each element on the left and right
                for another_seat in range(n):
                    if row[another_seat] == 0:
                        weight_left = 0
                        for i in range(another_seat - 1, -1, -1):
                            if row[i] != 0:
                                break
                            weight_left += 1
                        else:
                            weight_left = n
                        weight_right = 0
                        for i in range(another_seat + 1, n):
                            if row[i] != 0 or weight_left <= weight_right:
                                break
                            weight_right += 1
                        else:
                            weight_right = n
                        weight_seats[another_seat] = min(weight_left,
                                                         weight_right)
                # if max distance > 0 find index this place
                # and seat person there. Choose the one to the left
                max_weight = max(weight_seats)
                if max_weight > 0:
                    place_max_weight = weight_seats.index(max_weight)
                    person += 1
                    row[place_max_weight] = person
                else:
                    max_persons.append(person)
                    break
        # count number max seats for n place
        max_person = max_persons.count(max(max_persons))
        print('{} -> {}'.format(n, max_person))
        sum += max_person
    return sum


N = 20
print('Total: {} -> {}'.format(N, euler(N)))

assert euler(N) == 83

assert euler(-1) == 0
assert euler(0) == 0
assert euler(1) == 1
assert euler(2) == 3
assert euler(3) == 5
