# Создание вложенного кортежа-матрешки
nested_tuple = (3, (3.14, (2+3j, ("hello", ()))))


# Вывод всех элементов кортежа-матрешки
print("Целое число: ", nested_tuple[0])
print("Вещественное число: ", nested_tuple[1][0])
print("Комплексное число: ", nested_tuple[1][1][0])
print("Строка: ", nested_tuple[1][1][1][0])
print("Пустой кортеж: ", nested_tuple[1][1][1][1])
