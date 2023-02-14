# Program to demonstrate various functions and methods for strings in Python

def reverse_string(string):
  # Reverses the order of characters in a string
  return string[::-1]

def count_vowels(string):
  # Counts the number of vowels in a string
  vowels = "aeiouAEIOU"
  count = 0
  for char in string:
    if char in vowels:
      count += 1
  return count

def upper_case(string):
  # Converts all characters in a string to uppercase
  return string.upper()

def lower_case(string):
  # Converts all characters in a string to lowercase
  return string.lower()

def capitalize(string):
  # Capitalizes the first character of a string
  return string.capitalize()

def find_substring(string, sub_string):
  # Returns the index of the first occurrence of a substring in a string
  return string.find(sub_string)

def replace_substring(string, old, new):
  # Replaces all occurrences of a substring in a string with a new substring
  return string.replace(old, new)

def split_string(string, separator):
  # Splits a string into a list of substrings based on a separator
  return string.split(separator)

def join_strings(strings, separator):
  # Joins a list of strings into a single string using a separator
  return separator.join(strings)

def strip_whitespace(string):
  # Removes leading and trailing whitespace from a string
  return string.strip()

# Testing the functions
string = "Hello, World!"
sub_string = "World"
old = "World"
new = "Friend"
separator = " "
strings = ["Hello,", "World!"]

print("Reverse of the string:", reverse_string(string))
print("Number of vowels in the string:", count_vowels(string))
print("Uppercase of the string:", upper_case(string))
print("Lowercase of the string:", lower_case(string))
print("Capitalized string:", capitalize(string))
print("Index of the substring:", find_substring(string, sub_string))
print("String after replacing substring:", replace_substring(string, old, new))
print("Split string:", split_string(string, separator))
print("Join strings:", join_strings(strings, separator))
print("String after stripping whitespace:", strip_whitespace(string))
