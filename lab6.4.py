# Создание списка с названиями категорий расходов
categories = ['Транспорт', 'Обед', 'Продукты', 'Развлечения', 'Прочее']

# Создание списка списков для хранения расходов за каждый день недели
expenses = [[] for _ in range(7)]

# Ввод расходов за каждый день недели
for i in range(7):
    print("Расходы за день", i+1)
    for j in range(len(categories)):
        expense = float(input(categories[j] + ": "))
        expenses[i].append(expense)

# Вычисление общего объема расходов за неделю
total_expenses = sum([sum(expenses[i]) for i in range(7)])

# Вывод результатов
print("Общий объем расходов за неделю: ", total_expenses)
