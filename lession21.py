# задания 21.1

name = "Конвейер"

def change_name():
    name = "Вытяжка"
    print("Внутри функции:", name)

change_name() # вызывает функцию (name = "Вытяжка" переменная локальная, которая существует только внутри функции)
print("Снаружи функции:", name) # выводит значение переменной name, которая была определена вне функции (name = "Конвейер") это снаружи функции, глобальная переменная, которая существует в основном коде программы

# задания 21.2
voltage = 380

def change_voltage(voltage):
    voltage = 220
    print("Внутри:", voltage)

change_voltage(voltage) # вызывает функцию (voltage = 220 переменная локальная, которая существует только внутри функции)

print("Снаружи:", voltage) # выводит значение переменной voltage, которая была определена вне функции (voltage = 380) это снаружи функции, глобальная переменная, которая существует в основном коде программы

# задания 21.3
motors = [
    {"name": "Конвейер", "status": "OFF"},
    {"name": "Вытяжка", "status": "ON"}
]

def turn_off_motor(motors):
    for motor in motors:
        if motor["name"] == "Вытяжка" and motor["status"] == "ON":
            motor["status"] = "OFF"
    return motors
print("Состояние моторов до вызова функции:", motors)
motors = turn_off_motor(motors)
print("Состояние моторов после вызова функции:", motors)
turn_off_motor(motors) # вызывает функцию (меняет статус мотора "Вытяжка" на "OFF")