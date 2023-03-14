# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно. Также заполните второй кортеж числами от -5 до 0.
# Для заполнения кортежей числами напишите одну функцию. Объедините два кортежа с помощью оператора +, создав тем самым третий кортеж.
# С помощью метода кортежа count() определите в нем количество нулей. Выведите на экран третий кортеж и количество нулей в нем.

import random

#min_num-tan max_num-ga deingi sandarmen kortejdi toltyratyn funksia
def fill_tuple(size, min_num, max_num):
    return tuple(random.randint(min_num, max_num) for _ in range(size))

# kortejderdi tolrtyru
tuple1 = fill_tuple(10, 0, 5)
tuple2 = fill_tuple(10, -5, 0)

# Kortejderdi biriktiru
tuple3 = tuple1 + tuple2

# Kortejdegi nolderdi sanau
zeros_count = tuple3.count(0)

# Natijeni shygaru
print("Birinshi kortej:", tuple1)
print("Ekinshi kortej:", tuple2)
print("Ushinshi kortej:", tuple3)
print("Ushinshi kortejdegi nolder sany:", zeros_count)
