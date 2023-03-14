# Сөздіктерге байланысты 5 функция немесе əдістерді қолданып
# бағдарлама жазу қажет.

#
# Dictionaries are used to store data values in "key:value" pairs.
#
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


# Bos sozdik jasau
students = {}

# update() adisin qoldanyp birneshe jana element qosamyz
students.update({"John": 21, "Alice": 19})
students.update({"Bob": 20, "Mary": 22})
students.update({"Mike": 23, "Alex": 25})

#keys() adisimen sozdiktin kiltterin shygaramyz
print("Sozdiktin kiltteri:")
print(*students.keys())

# values() adisimen sozdik manderin shygaramyz
print("Sozdiktin manderi:")
print(*students.values())

# items() adisimen sozdiktin elementterin shygaru
print("Sozdiktin elementteri:")
print(*students.items())

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print('Sozdik: ', thisdict)

# update() adisimen elementtin manin ozgertemiz
students.update({"Alice": 20})

#pop() adisimen elementti joiamyz
students.pop("Bob")

# Natizheni shygaru
print("Natizhe:")
print(*students.items())
