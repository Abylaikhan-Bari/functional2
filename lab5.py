students = {
    "Alice": ["Math", "Science", "English"],
    "Bob": ["History", "Math", "Art"],
    "Charlie": ["English", "Science", "History"]
}

# Функция, которая выводит список предметов, которые изучает ученик
def print_subjects(student):
    print(f"{student} изучает следующие предметы:")
    for subject in students[student]:
        print(subject)

# Функция, которая добавляет новый предмет в список ученика
def add_subject(student, subject):
    students[student].append(subject)
    print(f"Предмет {subject} добавлен в список {student}")

# Функция, которая удаляет предмет из списка ученика
def remove_subject(student, subject):
    if subject in students[student]:
        students[student].remove(subject)
        print(f"Предмет {subject} удален из списка {student}")
    else:
        print(f"{student} не изучает предмет {subject}")

# Функция, которая возвращает список всех учеников
def get_students():
    return list(students.keys())

# Функция, которая находит ученика с наибольшим количеством предметов
def find_most_subjects():
    most_subjects = 0
    most_subjects_student = ""
    for student, subjects in students.items():
        if len(subjects) > most_subjects:
            most_subjects = len(subjects)
            most_subjects_student = student
    return most_subjects_student

# Пример использования функций
print_subjects("Alice")
add_subject("Bob", "Science")
remove_subject("Charlie", "Math")
print(get_students())
print(find_most_subjects())
