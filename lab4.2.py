def convert_case(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    if upper_count > lower_count:
        return string.upper()
    else:
        return string.lower()

input_string = input("Enter a string: ")
result = convert_case(input_string)
print("Result:", result)
