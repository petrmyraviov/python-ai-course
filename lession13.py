# Задания 1 лекция 13 
print("Введитет текст")
text = input()
print(f"Исходный текст:\n{text}")
print(f"Верхний регистор:\n{text.upper()}")
print(f"Нижний регистр:\n{text.lower()}")
print(f"Каждое слово с большой буквы:\n{text.title()}")
text_title = text.title()
print(f"Заменить Python на Siemens:\n{text_title.replace("Python", "Siemens")}")
# Задания 2  лекция 13 
# text = "hello"
# text.upper()
# print(text)
# ответ потому что text.upper() переменная с методом печатает новую страку , 
# тоесть нужно создать новую переменую чтобы данные сохранить text_upper = text.upper()
# а так мы просото вызываем print(text) без каких либо изменений , 