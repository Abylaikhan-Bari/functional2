# В первой строке содержится число N — число элементов в словаре. Дан список (словарь) стран и рек, протекающих в каждой стране. Затем даны
# названия рек	(в виде списка). Выполните задания:
# 1)	Для каждой реки укажите, в какой стране она протекает.
# 2) Проверьте, есть ли введенное назван ие реки в словаре (вывести есть или нет)
# 3) Добавьте новую пару страна-река в словарь.
# Считываем число элементов в словаре

n = int(input("Jalpy sany: "))

# Создаем пустой словарь
dictionary = {}

# Считываем пары страна-река и добавляем их в словарь
for i in range(n):
    country, river = input("El men ozen engiziniz: ").split()
    if country not in dictionary:
        dictionary[country] = [river]
    else:
        dictionary[country].append(river)

# Считываем название реки для проверки наличия в словаре
check_river = input("Tekseretin ozen atyn engiziniz: ")

# Проверяем наличие названия реки в словаре
if any(check_river in rivers for rivers in dictionary.values()):
    print("Bar")
else:
    print("Joq")

# Добавляем новую пару страна-река в словарь
new_country, new_river = input("Jana el men ozen engiziniz: ").split()
if new_country not in dictionary:
    dictionary[new_country] = [new_river]
else:
    dictionary[new_country].append(new_river)

# Выводим для каждой реки страну, в которой она протекает
for river in sorted(set(sum(dictionary.values(), []))):
    for country, rivers in dictionary.items():
        if river in rivers:
            print(f"{river} - {country}")
