# Задания 27.1
def get_motor_data():
    return  "Конвейер", 15
name, power = get_motor_data() # Распакуй кортеж, который возвращает функция get_motor_data() в две переменные name и power.
print(f"Название двигателя: {name}, мощность двигателя: {power} кВт")

# Задания 27.2
def check_voltage(voltage):
    if voltage <= 0:
        return "Напряжение должно быть положительным", False
    return "Напряжение допустимо", True
print(check_voltage(380)) # Выведи результат вызова функции на экран. (возвращает True)
print(check_voltage(0)) # Выведи результат вызова функции на экран. (возвращает False)  

# Задания 27.3
try:
    voltage = int(input("Введите напряжение двигателя в В: "))
    message, valid = check_voltage(voltage) # Распакуй кортеж, который возвращает функция check_voltage() в две переменные message и valid.
    if valid == True: # Используй оператор моржового присваивания (:=) для проверки значения valid.
        print(f"{message}: {voltage} В, проверка: {valid}")
    print(f"{message} {voltage} В, проверка: {valid}")
except ValueError:
    print("Ошибка: введите целое число")

