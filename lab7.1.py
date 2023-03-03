# Сөздіктерге байланысты 5 функция немесе əдістерді қолданып
# бағдарлама жазу қажет.

# Создание пустого словаря
my_dict = {}

# Добавление элементов в словарь
my_dict["apple"] = 2
my_dict["banana"] = 4
my_dict["orange"] = 1

# Получение значения по ключу
print("У меня есть", my_dict["apple"], "яблок")

# Удаление элемента из словаря по ключу
del my_dict["orange"]

# Проверка наличия ключа в словаре
if "banana" in my_dict:
    print("У меня есть", my_dict["banana"], "бананов")

# Получение списка ключей и значений из словаря
keys = list(my_dict.keys())
values = list(my_dict.values())

print("В моем холодильнике есть:")
for i in range(len(keys)):
    print(keys[i], "-", values[i])

# Обновление словаря с помощью другого словаря
new_dict = {"grape": 3, "pear": 2}
my_dict.update(new_dict)

print("После похода в магазин в моем холодильнике есть:")
for key, value in my_dict.items():
    print(key, "-", value)
