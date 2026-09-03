# Задания 1, Лекция 14
print("Введите текст")
text = input()
print(f"Исходный текст:\n{text}")
print(f"После strip():\n{text.strip()}")
text_strip = text.strip()
print(f"Количество слов Python:\n{text_strip.count("Python")}")
print(f"Индекс первого слово Python:\n{text_strip.find("Python")}")
print(f"Начинается с \"I\":\n{text_strip.startswith("I")}")
print(f"Заканчивается на \"Python\":\n{text_strip.endswith("Python")}")

# Задания 2, Лекция 14
text = "banana"

print(text.find("a"))          # Индекс 1
print(text.find("na"))         # Индекс 2
print(text.count("na"))        # Найдет все "na" в слове  вернет 2
print(text.startswith("ban"))  # Он вернет True 
print(text.endswith("ana"))    # Будет True