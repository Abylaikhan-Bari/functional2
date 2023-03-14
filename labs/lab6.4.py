# Общий объем расходов. Разработайте программу, которая подсчитает ваши расходы за каждый день недели.
# Расходы по следующим категориям (транспортные расходы, обед, и т.д.) Суммы должны быть сохранены в списке.
# Примените цикл, чтобы вычислить общий объем расходов за неделю и показать результат.


# Создаем пустой словарь для расходов
expenses = {}

# Создаем список дней недели
weekdays = ['Duisenbi', 'Seisenbi', 'Sarsenbi', 'Beisenbi', 'Juma', 'Senbi', 'Jeksenbi']

# Просим пользователя ввести расходы за каждый день недели
for day in weekdays:
    expenses[day] = {}
    print(f'{day} kunnin shygyny :')
    expenses[day]['kolik'] = float(input('Kolik: '))
    expenses[day]['tagam'] = float(input('Tuski as: '))
    expenses[day]['oiyn-sauyq'] = float(input('Oiyn-sauyq: '))

# Вычисляем общую сумму за неделю
total_expenses = 0
for day in expenses:
    total_expenses += sum(expenses[day].values())

# Выводим результат
print('\nBir aptanyn shygyny:')
for day in expenses:
    print(f'{day}: {sum(expenses[day].values())} tenge.')

print("\n")
print(f'Jalpy apta shygyny: {total_expenses} tenge.')