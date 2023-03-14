#Напишите программу, которая любой введенный казахский текст из кириллицы переводит в латиницу.

from transliterate import translit

text = input("Қазақша сөз енгізіңіз: ")
transliterated_text = translit(text, 'ru', reversed=True)

print("Engizilgen soz latyn aripterimen: ", transliterated_text)
