# 1 Задания, функция произведение двух чисел
def multiply(a, b):
    return a * b
# Пример использования
result = multiply(5, 8)
print(result)  # Вывод: 15

# 2 Задания, функция определения возраста 
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
# Пример использования
print(is_adult(20))  # Вывод: True
print(is_adult(15))  # Вывод: False

# 3 Задания, функция возращения большего числа из двух
def max_number(a, b):
    if a > b:
        return a
    else:
        return b
# Пример использования
print(max_number(15, 9))  # Вывод: 15

# 4 Задания, функция возращает среднее значения
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
# Пример использования
print(calculate_average([1, 2, 3, 4, 5]))

