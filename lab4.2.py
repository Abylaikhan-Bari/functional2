'Вводится строка, включающая строчные и прописные буквы. Требуется вывести ту же строку в одном регистре, \
который зависит от того, каких букв больше. При равном количестве преобразовать в нижний регистр. \
Например, вводится строка "HeLLo World", она должна быть преобразована в "hello world", потому что в исходной строке малых букв больше.\
В коде используйте цикл for, строковые методы upper() (преобразование к верхнему регистру) и lower() (преобразование к нижнему регистру),\
а также методы isupper() и islower(), проверяющие регистр строки или символа.'
def convert_case(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    if upper_count > lower_count:
        print("\nupper kop")
        return string.upper()
    else:
        print("\nlower kop")
        return string.lower()

input_string = input("Joldy engiziniz: ")
result = convert_case(input_string)
print("\nNatizhe:", result)
