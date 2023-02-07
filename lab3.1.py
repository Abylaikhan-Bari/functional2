'for және while циклдарды қолданып жеке программа құру'

print("Sandardyn ortasha manin anyqtau:")
p = int(input("\nNeshe san: "))
sum = 0
count = 0

for i in range(1, p+1):
    count += 1
    san = int(input("San " + str(i) + ": "))
    sum += san

average = sum / count
print("Sandardyn ortahsha mani:", average)

print("\nSandardyn kvadraty: ")
n = int(input("\nNesheden: "))
m = int(input("Neshege deyin: "))
while n <= m:
    kvadrat = n**2
    print(n, 'sanynyn kvadaraty: ',kvadrat)
    n += 1