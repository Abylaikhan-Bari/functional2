# Əртүрлі топтардағы студенттерді əртүрлі пəндер бойынша секцияға
# қатысатын бағдарлама жазыңыз. Тізімді əртүрлі санаттарға байланысты
# сұрыптау қажет. Нəтижені экранда көрсетіңіз.
# Напишите программу, в которой предлагается вводить учащихся
# различных групп, посещающих секции по разным предметам. Требуется
# упорядочить список по различным категориям. Вывести результат на
# экран.

from itertools import groupby

students = []

# Studentter tizimin toltyru
while True:
    student = {}
    student['name'] = input('Studenttin aty joni (nemese toqtatu ushin "stop"): ')
    if student['name'] == 'stop':
        break
    student['group'] = input('Toptyn rettik sany: ')
    student['subject'] = input('Pandi engiziniz: ')
    students.append(student)

# Tizimdi toptar boiynsha suryptau
students.sort(key=lambda x: x['group'])

# Tizimdi toptar jane pander boiynsha shygaru
for group, students_in_group in groupby(students, key=lambda x: x['group']):
    print(f'Top {group}:')
    for student in students_in_group:
        print(f'\t{student["name"]}, {student["subject"]}, qatysady')

