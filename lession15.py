# Задания 1, Лекчия 15
print("Введите текст:")
text = input()
print(f"Исходный текст:\n{text}")
text_split = text.split()
print(f"Список через метод \"split()\":\n{text_split}")
print(f"Количество слов len() списка:\n{len(text_split)}")
print(f"Первое слово списка:\n{text_split[0]}")
print(f"Последнее слово списка:\n{text_split[3]}")