# Напишите программу, которая поможет находить номера телефонов по имени.
#
# В первой строке задано одно целое число - количество номеров телефонов.
# В следующих строках заданы телефоны и имена их владельцев через пробел.
# В следующей строке записан запрос — это имя, чей телефон нужно найти.
# Вывести номер телефона согласно запросу. Если в телефонной книге нет телефонов человека с таким именем,
# выведите в соответствующей строке «Нет в телефонной книге».

# jalpy sanyn alu
n = int(input("Nomir sany: "))

# Telefon men nomir saqtaityn sozdik jasaimyz
phone_book = {}

# Telefon men attaryn saqtaimyz
for i in range(n):
    phone, name = input("Telefon jane esimi: ").split()
    phone_book[name] = phone

# Izdep, shygaru
query_name = input("Izdeu: ")
if query_name in phone_book:
    print('Natizhe: ', phone_book[query_name])
else:
    print("Telefon kitapshasynda joq!")
