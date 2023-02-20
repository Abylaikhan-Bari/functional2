from itertools import groupby

students = []

# заполнение списка учащихся
while True:
    student = {}
    student['name'] = input('Введите имя учащегося (или "стоп" для завершения ввода): ')
    if student['name'] == 'стоп':
        break
    student['group'] = input('Введите номер группы: ')
    student['subject'] = input('Введите предмет, который посещает учащийся: ')
    students.append(student)

# сортировка списка по группам
students.sort(key=lambda x: x['group'])

# вывод списка по группам и предметам
for group, students_in_group in groupby(students, key=lambda x: x['group']):
    print(f'Группа {group}:')
    for student in students_in_group:
        print(f'\t{student["name"]}, посещает {student["subject"]}')
