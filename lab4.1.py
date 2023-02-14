students = []

while True:
    student = input("Введите ФИО ученика (для завершения ввода введите 'q'): ")
    if student == 'q':
        break
    grade = input("Введите класс ученика: ")
    students.append((student, int(grade)))

students.sort(key=lambda x: x[1])

for student, grade in students:
    print(f"{student}, {grade} класс")
