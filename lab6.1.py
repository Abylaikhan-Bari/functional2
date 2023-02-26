# Функция, которая создает и возвращает кортеж из заданных элементов
def create_tuple(*elements):
    return tuple(elements)

# Функция, которая объединяет два кортежа и возвращает новый кортеж
def merge_tuples(tuple1, tuple2):
    return tuple1 + tuple2

# Функция, которая создает и возвращает множество из заданных элементов
def create_set(*elements):
    return set(elements)

# Функция, которая объединяет два множества и возвращает новое множество
def merge_sets(set1, set2):
    return set1.union(set2)

# Функция, которая находит пересечение двух множеств и возвращает новое множество
def find_intersection(set1, set2):
    return set1.intersection(set2)

# Пример использования функций
tuple1 = create_tuple(1, 2, 3)
tuple2 = create_tuple(4, 5, 6)
print("Кортеж 1:", tuple1)
print("Кортеж 2:", tuple2)
merged_tuple = merge_tuples(tuple1, tuple2)
print("Объединенный кортеж:", merged_tuple)

set1 = create_set(1, 2, 3)
set2 = create_set(3, 4, 5)
print("Множество 1:", set1)
print("Множество 2:", set2)
merged_set = merge_sets(set1, set2)
print("Объединенное множество:", merged_set)
intersection = find_intersection(set1, set2)
print("Пересечение множеств:", intersection)
