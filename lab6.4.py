# Общий объем расходов. Разработайте программу, которая подсчитает ваши расходы за каждый день недели.
# Расходы по следующим категориям (транспортные расходы, обед, и т.д.) Суммы должны быть сохранены в списке.
# Примените цикл, чтобы вычислить общий объем расходов за неделю и показать результат.


# Kategorialar tizimi
categories = ['Kolik', 'Tuski as', 'Azyq-tulik', 'Oiyn-sauyq', 'Basqa narseler']

# Shygyndar tizimi
expenses = [[] for _ in range(7)]

# Aptanyn ar kunine shygyndardy engizu
for i in range(7):
    print("Bir kundik shygyn", i+1)
    for j in range(len(categories)):
        expense = float(input(categories[j] + ": "))
        expenses[i].append(expense)

# Bir apta boiynsha jalpy shygyndy esepteu
total_expenses = sum([sum(expenses[i]) for i in range(7)])

# Natijeni shygaru
print("Bir apta boiynsha shygyndar: ", total_expenses)
