# создаем пустой список
numbers = []

# заполняем список числами, пока пользователь не введет 0
while True:
    num = int(input('Введите целое число (0 для завершения ввода): '))
    if num == 0:
        break
    numbers.append(num)

# сортируем список по возрастанию
numbers.sort()

# выводим список на экран
for num in numbers:
    print(num)
