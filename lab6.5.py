# Вводятся имена студентов в одну строчку через пробел. На их основе формируется кортеж.
# Отобразите на экране все имена из этого кортежа, которые содержат фрагмент "ва". Имена выводятся в одну строку через пробел.



# Studentterdin atyn engizu
students_str = input("Bos oryn arqyly studentterdin attaryn engiziniz: ")

# Engizilgen attardan kortej jasau
students_tuple = tuple(students_str.split())

# "ва" bar barlyq attardy shygaru
va_names = [name for name in students_tuple if "ва" in name]
print("Esiminde 'ва' bar barlyq studentter:", " ".join(va_names), "\n")
