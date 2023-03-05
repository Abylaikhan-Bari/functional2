# Сөздіктерге байланысты 5 функция немесе əдістерді қолданып
# бағдарлама жазу қажет.

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

# update() adisimen elementtin manin ozgertemiz
students.update({"Alice": 20})

#pop() adisimen elementti joiamyz
students.pop("Bob")

# Natizheni shygaru
print("Natizhe:")
print(*students.items())
