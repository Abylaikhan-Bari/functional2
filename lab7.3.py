# В аккаунте социальной сети одного звезды прокомментировали фотографию. Некоторые посетители оставляли несколько комментариев. Требуется по списку комментариев определить уникальное число комментаторов. Комментарии поступают на вход программы в формате: имя 1: комментарий 1 имя 2: комментарий 2
#
# ...
# имя N: комментарий N
# пока не будет введена пустая строка. Также полагается, что имена у разных комментаторов не совпадают. Вывести на экран общее число уникальных комментаторов.
# Создаем пустое множество для хранения уникальных имен комментаторов

comments = {}
while True:
    input_string = input()
    if not input_string:
        break
    name, comment = input_string.split(": ")
    if name in comments:
        comments[name] += 1
    else:
        comments[name] = 1
print(len(comments))

