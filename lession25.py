# # задание 25.1
# try:
#     print("введите мощность двигателя в кВт")
#     power = float(input())
#     if power <= 0 :
#         print("Ошибка: введите число больше нуля")
#     else:
#         print(f"мощность двигателя: {power} кВт")
# except ValueError:
#     print("Ошибка: введите число больше нуля")

# # задание 25.2
# try:
#     print("Введите название двигателя")
#     name = input().split()
#     if not name:
#         print("Ошибка: введите название двигателя")
#     else:
#         print(f"название двигателя: {name}")
# except Exception as e:
#     print(f"Ошибка: {e}")

# задание 25.3
while True:
    try:
        print("ВВедите мощность двигателя в кВт")
        power = int(input())
        if power <= 0:
            raise ValueError("Ошибка: введите число больше нуля")
        elif power >= 15:
            raise ValueError("Ошибка: введите число меньше 15")
        else:
            print(f"мощность двигателя: {power} кВт")
            break
    except Exception as e:
        print(f"Ошибка: {e}")