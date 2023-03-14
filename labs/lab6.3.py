# Создайте кортеж-матрешку, в который поместите два элемента: целое число и вложенный кортеж, в который поместите еще два элемента:
# вещественное число и вложенный кортеж, в который поместите еще два элемента: комплексное число и вложенный кортеж,
# в который поместите еще два элемента: строку и пустой кортеж. Выведите на экран конечную строку.



# Kiristirilgen kortej-matreshka jasau
nested_tuple = (3, (3.14, (2+3j, ("Salem Alem!!!", ()))))


# Kortej-matreshkanyn barlyq elementterin shygaru
print("Butin san: ", nested_tuple[0])
print("Naqty san: ", nested_tuple[1][0])
print("Kompleks san: ", nested_tuple[1][1][0])
print("Jol(string): ", nested_tuple[1][1][1][0])
print("Bos kortej: ", nested_tuple[1][1][1][1])
