'Для настольной игры используются карточки с номерами от 1 до N.'
'Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.'
'Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). ' \
'Программа должна вывести номер потерянной карточки.'
'Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.'
def karta_tabu(n, kartalar):
    kerek_summa = n * (n + 1) // 2
    naqty_summa = 0
    for karta in kartalar:
        kerek_summa += karta
        print(kerek_summa)
    return kerek_summa - naqty_summa

n = int(input("Kartalardyn jalpy sany:"))
kartalar = [int(input("Qalgan kartalar:")) for i in range(n - 1)]
print(karta_tabu(n, kartalar))
