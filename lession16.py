# Задания 1. лекция 16
machines = [
    "Конвейер",
    "насос",
    "Компрессор",
    "Вентилятор"
]
for machine in machines:
    print(machine)

#  Задания 2, Лекция 16
for i, item in enumerate(machines):
    print(i, item)

#  Задания 3, Лекция 16
numbers = [10, 20, 30]

for number in numbers:
    number = number + 5

print(numbers)
# Список не увиличится потому что мы вызываем массив numbers а не переменую которая number вот она изменила 