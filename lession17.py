#  Задания 1. Лекция 17
machines = ["Конвейер","Насос"]
machines.append("Компрессор")
for machine in machines:
    print(machine)

#  Задания 2. Лекция 17
machines.insert(2, "Вентилятор")
for machine in machines:
    print(machine)

#  Задания 3. Лекция 17
machines.remove("Насос")
for machine in machines:
    print(machine)

#  Задания 4. Лекция 17
deleted_machine = machines.pop()
print(f"Удалённый элемент:\n{deleted_machine}")
print("Оставшийся список:")
for machine in machines:
    print(machine)

# Задания 5. Лекция 17
machines.clear()
print(machines)