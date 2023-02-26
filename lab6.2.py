import random

# Функция, которая заполняет кортеж числами от min_num до max_num
def fill_tuple(size, min_num, max_num):
    return tuple(random.randint(min_num, max_num) for _ in range(size))

# Заполнение кортежей
tuple1 = fill_tuple(10, 0, 5)
tuple2 = fill_tuple(5, -5, 0)

# Объединение кортежей
tuple3 = tuple1 + tuple2

# Подсчет количества нулей в кортеже
zeros_count = tuple3.count(0)

# Вывод результатов
print("Первый кортеж:", tuple1)
print("Второй кортеж:", tuple2)
print("Третий кортеж:", tuple3)
print("Количество нулей в третьем кортеже:", zeros_count)
