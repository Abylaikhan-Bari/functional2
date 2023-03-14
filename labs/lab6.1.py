# Кортежмен (tuple) жəне жиындармен (Set) жұмыс істеу үшін кемінде 5 функцияны қолданып программа жазыңыз.

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

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
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)



set1 = create_set(1, 2, 3)
set2 = create_set(3, 4, 5)

print("Set 1:", set1)
print("Set 2:", set2)
merged_set = merge_sets(set1, set2)
print("Biriktirilgen set:", merged_set)
intersection = find_intersection(set1, set2)
print("Jiyndardyn qilysuy:", intersection)

thisset = {"apple", "banana", "cherry"}

print("Set 3: ", thisset)
print("Settegi element sany: ", len(thisset))
print("Set 3 datatype:", type(thisset))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))