# Создайте словарь с помощью генератора словарей, так чтобы его ключами были
# числа от 1 до 20, а значениями кубы этих чисел.
dct = {num: num ** 3 for num in range(1, 21)}
print(dct)
