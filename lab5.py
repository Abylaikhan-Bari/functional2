# Тізімде қолданылатын кемінде 5 функциядарды қолданып,
# программа жазып шығу. Тізім ретінде əр студент өзінің
# резюмесін ұсынсын. Жəне сол тізіммен жұмыс жасасын.

# Tizim quru
my_list = [1, 2, 3, 4, 5]

# Tizim uzundygy
print(len(my_list))

# Tizimnin sonyna element qosady
my_list.append(6)
print(my_list)

# Tizimnin belgili bir jerine element qosasdy
my_list.insert(2, 7)
print(my_list)

# Tizimnin songy elementin joiady
last_element = my_list.pop()
print(last_element)
print(my_list)

# Tizimdi osu retimen suryptaidy
my_list.sort()
print(my_list)
