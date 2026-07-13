# Первое задание
for number in range(1, 21): 
    print(number)
# Второе задание
for number in range(20, 0, -1):
    print(number)

# Третье задание
number_first = int(input("Введите число:\n"))
if (number_first) > 0:
    for number in range(1, 11):
        total = number_first * number
        print(f"{number_first} * {number} = {total}")
else:
    print("Вы ввели что-то не то!")


# Четвертое задание
temperatures = []
for temperature in range(1, 6):
    temperatures.append(int(input(f"Введите температуру двигателя №{temperature}:\n" )))
print(f"Общая температура: {sum(temperatures)}")