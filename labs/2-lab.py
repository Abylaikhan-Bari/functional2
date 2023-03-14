# Studenttin atyn surap, onyn stipendia alu mumkindigin tekseretin bagdarlama

# Studenttin atyn surau
name = input("Studenttin aty: ")

# Qosymsha aqparat alu
info = input("Salem " + name + " stipendia alu mumkindigin tekseru? (ia nemese joq) ")

# Studenttin stipendia alu mumkindigin tekseru ushin if else qoldanamyz
if info == "ia":
    print("\n" + name + " stipendia alu mumkindigin tekseru.")

    sabaq1 = float(input("1-sabaq bally: "))
    if sabaq1 > 100:
        print("Qate!")
    sabaq2 = float(input("2-sabaq bally: "))
    if sabaq2 > 100:
        print("Qate!")
    sabaq3 = float(input("3-sabaq bally: "))
    if sabaq3 > 100:
        print("Qate!")
    sabaq4 = float(input("4-sabaq bally: "))
    if sabaq4 > 100:
        print("Qate!")

    ortasha = float((sabaq1 + sabaq2 + sabaq3 + sabaq4)/4)

    if 50 <= ortasha < 90:
        print("\n" + name + " stipendia alady!")
        print("Ortasha baly: ")
        print(float(ortasha))

    elif float(ortasha) > 90:
        print("Qate!")
        print("Ortasha baly: ")
        print(float(ortasha))
    else:
        print("\n" + name + " stipendia almaidy!")
        print("Ortasha baly: ")
        print(float(ortasha))

