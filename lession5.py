age = int(input("Cколько тебе лет?\n"))
if age >= 18 and age < 150:
    print("Добро пожаловать!")
elif age > 150:
    print("Ты что, из будущего?")
else:
    print("Доступ запрещен!")

temperature = int(input("Температура двигателя:\n"))
if temperature < 60:
    print("Двигатель холодный  ")
elif temperature >= 60 and temperature < 80:
    print("Двигатель нормальный")
else:
    print("Двигатель перегрет!")