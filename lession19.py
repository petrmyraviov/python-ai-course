# Задания 1. Лекция 19
motor = {
    "power": 15,
    "voltage": 380,
    "frequency": 50
}
for motors in motor:
    print(motors)

#  Задания 2, Лекция 19
motor["voltage"] = 220
for i, motors in enumerate(motor):
    print(motor)