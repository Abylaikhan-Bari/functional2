# Кортежмен (tuple) жəне жиындармен (Set) жұмыс істеу үшін кемінде 5 функцияны қолданып программа жазыңыз.


# Belgilengen elementterden tuple (kortej) jasap, sony qaitaratyn funksia
def create_tuple(*elements):
    return tuple(elements)

#Eki kortejdi biriktirip, jana kortej qaitaratyn funksia
def merge_tuples(tuple1, tuple2):
    return tuple1 + tuple2

#Belgilengen elementterden jiyn jasap, sony qaitaratyn funksia
def create_set(*elements):
    return set(elements)

# Eki jiyndy biriktirip jana jiyn jasaityn funksia
def merge_sets(set1, set2):
    return set1.union(set2)

#Eki jiynnyn qiylysyn tauyp, jana jiyn qaitaratyn funksia
def find_intersection(set1, set2):
    return set1.intersection(set2)

# Funksialardy qoldanu
tuple1 = create_tuple(1, 2, 3)
tuple2 = create_tuple(4, 5, 6)
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
merged_tuple = merge_tuples(tuple1, tuple2)
print("Biriktirilgen tuple:", merged_tuple)

set1 = create_set(1, 2, 3)
set2 = create_set(3, 4, 5)
print("Set 1:", set1)
print("Set 2:", set2)
merged_set = merge_sets(set1, set2)
print("Biriktirilgen set:", merged_set)
intersection = find_intersection(set1, set2)
print("Jiyndardyn qilysuy:", intersection)
