'range() функциясын қолданып тізім жасау. range() функциясына'
'әртүрлі типтегі мәндерді еңгізіп. әртүрлі мысалдар арқылы нәтижесін экранға шығару'
'randint() randrange() random() enumerate() функцияларын өз бағдарламаңызда қолдану'

import random

start = int(input("Start: "))
end = int(input("End: "))

My_list1 = [*range(start, end+1, 1)]

print(My_list1)

basy = int(input("\nBasy: "))
sony = int(input("Sony: "))
qadamy = int(input("Qadamy: "))

san1 = random.randint(basy, sony)
san2 = random.randrange(basy, sony, qadamy)


My_list2 = [*range(san1, san2+1, 1)]
print(My_list2)