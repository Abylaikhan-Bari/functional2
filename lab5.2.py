# Тізім қайтаратын функция жазып шығу. Алдын ала студенттердің
# пəндері жəне бағалары бар тізім құрастыр. Жəне сол тізім бойынша
# студенттің атын еңгізген кезде, сол студенттің бағаларын шығарып
# бертін болсын.
# Напишите программу которая возвращает список. Заранее подготовьте
# список предметов и оценок учащихся. Когда вы вводите имя учащегося, то
# должны отображаться оценки этого учащегося.


# Bagalar men attar bar tizim
grades = {
    'Max': {'math': 4, 'physics': 5, 'chemistry': 3},
    'Alex': {'math': 5, 'physics': 4, 'chemistry': 5},
    'Marty': {'math': 3, 'physics': 4, 'chemistry': 4},
}

# Oqushynyn atyna qarap bagalaryn shygaru
while True:
    name = input('Studenttin aty joni (nemese toqtatu ushin "stop"): ')
    if name == 'stop':
        break
    if name in grades:
        print(f'{name} bagalary: ')
        for subject, grade in grades[name].items():
            print(f'{subject}: {grade}')
    else:
        print(f'{name} degen oqushy joq!!!')
