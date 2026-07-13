cout = 1
while cout <= 10:
    print(f"Это твой {cout} раз!")
    cout += 1

count = 2
while count <= 10:
    print(f"Это твой {count} раз!")
    count += 2

password = int(input("Введите пароль:\n"))
while password != 1234:
    print("Неверный пароль!")
    password = int(input("Введите пароль:\n"))
    if password == 1234:
        print("Добро пожаловать!")
