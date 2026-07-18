# Лекция 11, практика 
print("Введите имя:")
name = input()
print("Количество символов: ", len(name))
print("Первый символ: ", name[0])
print("Последний символ: ", name[-1])
print("Все символы:")
for letter in name:
    print(letter)

print(f"Слово наоборот:\n{name[::-1]}")