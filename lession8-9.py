# 1 задания , функция приветствия
def hello():
    print("Добро пожаловать в программу!")
hello()

# 2 Задания, функция выводит квадрат числа
number = int(input("Введите число, чтобы узнать его квадрат: "))
def square(number):
    print(number ** 2)
square(number)

# 3 Задания, функция выводит температуру двигателя
temperature = int(input("Введите температуру двигателя: "))
def engine_temperature(temperature):
    if temperature < 60:
        print("Двигатель холодный")
    elif temperature >= 60 and temperature < 80:
        print("Двигатель нормальный")
    else:
        print("Двигатель перегрет!")
engine_temperature(temperature)

# 4 Задания, Функция работа двигателя
print("Введите состояние двигателя (True/False): ")
motor_status = input()
def motor(motor_status):
    if motor_status.lower() == "true":
        print("Двигатель работает")
    elif motor_status.lower() == "false":
        print("Двигатель не работает")
    else:
        print("Вы ввели что-то не то!")
motor(motor_status)