# Задания 28.1
def check_voltage(voltage):
    if voltage <= 0:
        return "Запуск запрещён: напряжение должно быть положительным", False
    elif voltage >= 380 and voltage < 450:
        return "Запуск запрещён: нет разрешения, Напряжение высокое", False
    elif voltage >= 450:
        return "Запуск запрещён: нет разрешения, Напряжение высокое", True
    return "Напряжение допустимо", True

def check_permission(permission):
    if permission == True and "Напряжение допустимо" == check_voltage(voltage)[0]:
        return "Разрешение получено", True
    elif "высокое" == check_voltage(voltage)[0] and check_voltage(voltage)[1] == True:
        return "Запуск запрещён: нет разрешения", True
    else:
        return "Запуск запрещён: нет разрешения", False
    
def can_start_motor(voltage):
    if voltage <= 0 and check_voltage(voltage)[1] == False:
        message, valid = check_voltage(voltage)
        return message, valid
    elif voltage >= 380 and voltage < 450 and check_voltage(voltage)[1] == True:
        message, valid = check_voltage(voltage)
        return message, valid
    elif voltage >= 450:
        message, valid = check_voltage(voltage)
        return message, valid
    message, valid = check_voltage(voltage)
    return message, valid


try:   
    voltage = int(input("Введите напряжение двигателя в В: "))
    message, can_start = can_start_motor(voltage)
    if can_start:
        print(f"{message}: {voltage} В, проверка: {can_start}")     
    else:
        print(f"{message}: {voltage} В, проверка: {can_start}") 
except ValueError:
    print("Ошибка: введите целое число")