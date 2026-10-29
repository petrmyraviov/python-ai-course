# Задания 26.1
def is_valid_power(power):
    if power <= 0:
        return False
    return True
print(is_valid_power(15)) # Выведи результат вызова функции на экран. (возвращает True)
print(is_valid_power(0)) # Выведи результат вызова функции на экран. (возвращает False)
# Задания 26.2
name = input("Введите название двигателя: ").strip()
def is_valid_name(name):
    if not name:
        return False
    return True

print(is_valid_name(name)) # Выведи результат вызова функции на экран. (возвращает True)