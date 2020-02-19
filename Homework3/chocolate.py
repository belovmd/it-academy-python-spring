def cut_kusok_area(n, m, k):
    """ Вернет True, если можно одним разломом отделить
        от шоколадки кусок площадью ровно k

        Площадь k и разлом это кратные длине и(или) ширине величины
        поэтому проверяем кратность k хотя бы одной из сторон.
        И площадь k должна быть <= площади шоколадки"""
    if (k % n == 0 or k % m == 0) and k <= n * m:
        return True
    return False


def cut_dolek(self, k):
    """Вернет True, если можно отломить от шоколадки (без ровно)
      k долек за некоторое количество разломов."""
    if k <= self.n * self.m:
        return True
    return False


def cut_dolek_razlomov(self, k, t):
    """ Вернет True, если можно отломить от шоколадки ровно
       k долек с помощью t разломов"""
    pass


print(cut_kusok_area(5, 8, 10))
print(cut_kusok_area(5, 8, 28))
