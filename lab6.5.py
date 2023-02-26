# Ввод имен студентов в одну строку через пробел
students_str = input("Введите имена студентов через пробел: ")

# Создание кортежа из введенных имен
students_tuple = tuple(students_str.split())

# Вывод всех имен из кортежа, содержащих фрагмент "ва"
va_names = [name for name in students_tuple if "ва" in name]
print("Имена, содержащие фрагмент 'ва':", " ".join(va_names))
