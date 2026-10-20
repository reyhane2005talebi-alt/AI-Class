words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "and": "و",
    "ai": "هوش مصنوعی",
    "hello": "سلام",
    "book": "کتاب",
    "school": "مدرسه",
    "water": "آب",
    "friend": "دوست"
}

sentence = "I love python and AI"

translated_count = 0
not_translated_count = 0

for word in sentence.split():
    word = word.lower()

    if word in words:
        print(words[word])
        translated_count += 1
    else:
        print(f"[{word}]")
        not_translated_count += 1

print("\nتعداد کلمات ترجمه شده:", translated_count)
print("تعداد کلمات ترجمه نشده:", not_translated_count)
