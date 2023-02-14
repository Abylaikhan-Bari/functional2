'Минимум 10 жолдарға арналған функциялар мен әдістерді қолданып бағларлама жазып шық.'

def length(string):
  #Tanba sanyn tabu
  return len(string)
def reverse_string(string):
  # Berilgen joldy kerisinshe shygarady
  return string[::-1]

def count_vowels(string):
  # Berilgen joldagy dauysty dybystardy sanaidy
  vowels = "aeiouywAEIOUYW"
  count = 0
  for char in string:
    if char in vowels:
      count += 1
  return count

def upper_case(string):
  # Joldagy barlyq z=simvoldardy jogargy registrge auystyrady
  return string.upper()

def lower_case(string):
  # Joldagy barlyq z=simvoldardy tomengi registrge auystyrady
  return string.lower()

def capitalize(string):
  # berilgen joldagy birinshi simvoldy jogargy registrge auystyrady
  return string.capitalize()

def replace_substring(string, old, new):
  # Joldagy bir sozdi auystyru
  return string.replace(old, new)

def split_string(string, separator1):
  # Berilgen joldyn sozderin bolek-bolek shygaru
  return string.split(separator1)

def join_strings(strings, separator2):
  # Joldar tizimin qosyp shygarady
  return separator2.join(strings)

def upper(string):
# Jogargy registrge tekseru
 return str.isupper(string)



string = input("Sozdi engiziniz: ")
old = input("Myna sozdi: ")
new = input("Mynagan auystyru: ")
separator1 = " "
separator2 = ""
strings = [input('Birinshi jol: '), input("Ekinshi jol: ")]

print("\n\n1) Dauysty tanbalar: ", count_vowels(string))
print("\n2) Joldyn kerisinshe turi: ", reverse_string(string))
print("\n3) Jogargy registrde: ", upper_case(string))
print("\n4) Tomengi registrde: ", lower_case(string))
print("\n5) Bas aripten bastalgan jol: ", capitalize(string))
print("\n6) Joldyn sozin auystyru: ", replace_substring(string, old, new))
print("\n7) Bolek sozder: ", split_string(string, separator1))
print("\n8) Joldar tizimin qosu: ", join_strings(strings, separator2))
print("\n9) Jol jogargy registrde me:", upper(string))
print("\n10) Joldagy tanbalar sany: ", length(string))



