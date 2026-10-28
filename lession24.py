# задания 24.1
print("Введите мощность двигателя в кВт:")
try:
    power = int(input())
    print(f"Мощность двигателя: {power} кВт")
except ValueError:
    print("Ошибка: введите целое число.")
    exit()
# задания 24.2
print("Введите знаменатель дробного числа:")
try:
    denominator = int(input())
    print("Введите числитель дробного числа:")
    numerator = int(input())
    print(f"Знаменатель дробного числа: {denominator}")
    print(f"Числитель дробного числа: {numerator}")
    result = numerator / denominator
    print(f"Результат деления: {result}")
except ValueError:
    print("Ошибка: введите целое число.")
    exit()
except ZeroDivisionError:
    print("Ошибка: деление на ноль.")
    exit()
# задания 24.3
while True: 
    try:
        print("Введите мощность двигателя в кВт:")
        power = int(input())
        print(f"Мощность двигателя: {power} кВт")   
        break
    except ValueError:
        print("Ошибка: введите целое число.")
