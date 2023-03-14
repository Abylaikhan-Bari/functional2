# Составьте словарь «График отпусков» для специалиста отдела кадров.
# По известному графику отпусков научитесь определять, у кого отпуск в заданном месяце.
#
# В	первой строчке записано целое число – количество сотрудников.
# В следующих N строчках записана информация о дате их отпуска.
# Каждая строчка состоит из трёх частей, разделённых пробелом – фамилии сотрудника, дня и месяца его отпуска.
#
# В	следующей строке записан запрос — это название месяца.
# Выведите через пробел фамилии всех сотрудников, у которых отпуск в указанном месяце.
# Если в заданном месяце никто не идет в отпуск, оставьте строку ответа пустой.


n = int(input("Qyzmetkerler sany: "))
vacations = {}

# Sozdikke aqparat engizu
for i in range(n):
    surname, day, month = input("Aty, kuni, aiy: ").split()
    if month not in vacations:
        vacations[month] = []
    vacations[month].append(surname)

# Belgilengen aida demalysta bolatyn qyzmetkerdi shygaru
month_query = input("Aidy engiziniz: ")
if month_query in vacations:
    print(f"{month_query} aiynda demalysta", ":")
    print(*vacations[month_query])
else:
    print("Bul aida eshkim demalysqa shyqpaidy.")
