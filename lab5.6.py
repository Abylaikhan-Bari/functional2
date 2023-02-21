# . Оған параметр ретінде берілген тізім сұрыпталғанын (өсу немесе кему
# ретімен) көрсететін функцияны жазыңыз. Тізім сұрыпталған болса, функция
# True мəнін, ал кері жағдайда False мəнін қайтаруы керек. Негізгі
# бағдарламада пайдаланушыдан тізімге арналған сандар тізбегін сұраңыз,
# содан кейін тізім бастапқыда сұрыпталғаны туралы хабарды көрсетіңіз.
# Напишите функцию, показывающую, отсортирован ли переданный ей
# в качестве параметра список (по возрастанию или убыванию). Функция
# должна возвращать True, если список отсортирован, и False в противном
# случае. В основной программе запросите у пользователя
# последовательность чисел для списка, после чего выведите сообщение
# о том, является ли этот список отсортированным изначально.

def is_sorted(lst):
    if all(lst[i] <= lst[i+1] for i in range(len(lst)-1)):
        # Eger arbir element aldyngy elementten ulken nemese ten bolsa, tizim osu retimen suryptalgan
        print('Tizim osu retimen suryptalgan')
        return True
    elif all(lst[i] >= lst[i+1] for i in range(len(lst)-1)):
        # Eger arbir element aldyngy elementten kishi nemese ten bolsa, tizim kemu retimen suryptalgan
        print('Tizim kemu retimen suryptalgan')
        return True
    else:
        # Nemese tizim suryptalmagan, iagni False
        return False

# Sandar tizbegin engizemiz
lst = list(map(int, input('"Space" arqyly sandardy engiziniz: ').split()))

# Tekseru funksiasyn shaqyramyz
if is_sorted(lst):
    print("")
else:
    print("Tizim suryptalmagan.")
