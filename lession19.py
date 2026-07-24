# Задания 1. Лекция 19
motor = {
    "power": 15,
    "voltage": 380,
    "frequency": 50
}
for motors in motor:
    print(motors, motor[motors])

#  Задания 2, Лекция 19
motor["voltage"] = 220
for i, motors in enumerate(motor):
    print(motors, motor[motors])

# задания 3, Лекция 19
motor["temperature"] = 75
for i, motors in enumerate(motor):
    print(motors, motor[motors])

#  Задания 4, Лекция 19
# Почему для хранения характеристик двигателя словарь удобнее, чем список?
# Потому что словарь имеет и нразвания и значения Индификационый ключ и значения , список только значения и номер индефикотор 