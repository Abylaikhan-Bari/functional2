'Напишите программу, в которой предлагается вводить учащихся различных груп, посещающих секции по программированию. \
Требуется упорядочить список по возрастанию классов. Распечатать список фамилий и классов'

students = []

while True:
    student = input("Aty joni (aiaqtau ushin 'q'): ")
    if student == 'q':
        break
    grade = input("Synyp: ")
    students.append((student, int(grade)))

students.sort(key=lambda x: x[1])

for student, grade in students:
    print(f"{student}, {grade} synyp")
