from transliterate import translit

text = input("Введите текст на казахском языке: ")
transliterated_text = translit(text, 'ru', reversed=True)

print("Текст на казахском языке в латинице: ", transliterated_text)
