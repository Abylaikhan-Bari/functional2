import random

# Генерируем 6 уникальных случайных чисел в диапазоне от 1 до 49
numbers = random.sample(range(1, 50), 6)

# Сортируем числа по возрастанию
numbers.sort()

# Выводим числа на экран
print("Номера билета:", numbers)
