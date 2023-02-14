while True:
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")

    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        print("The sum is:", a + b)
        break
    else:
        print("Invalid input, try again.")
