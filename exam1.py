
motor_runing = False
temperature = 25
count = 6
def imagel_manual():
    print("=============================")

def start_motor(motor_runing):
    if  motor_runing == False and temperature <=79:
        motor_runing = True
        print("Двигатель запущен")
        return motor_runing
    else:
        print("Двигатель уже работает")
def stop_motor(motor_runing):
    if  motor_runing == True:
        motor_runing = False
        print("Двигатель остановлен")
        return motor_runing
    else:
        print("Двигатель уже остановлен")
        return motor_runing
def show_motor_status(temperature, motor_runing):
    imagel_manual()
    print("Состояние двигателя:\n")
    if motor_runing == True:
        print("Двигатель работает\n")
        print(f"Температура двигателя: {temperature}°C\n")
        imagel_manual()
    else:
        print("Двигатель остановлен\n")
        print(f"Температура двигателя: {temperature}°C\n")
        imagel_manual()

def change_temperature(temperature):
    if temperature >= 80:
        motor_runing = False
        print("Запуск невозможен.\n двигатель перегрет.\n")
    else:
        motor_runing
    imagel_manual()
    print(f"\nТемпература двигателя: {temperature}°C\n")
    imagel_manual()
    return temperature

while count >1:
    imagel_manual()
    print("    УПРАВЛЕНИЕ ДВИГАТЕЛЕМ")
    imagel_manual()

    print("\n1. Запустите двигатель\n \n2. Остановите двигатель\n \n3. Измерте температуру двигателя\n \n4. Показать состояние двигателя\n \n5. Выйти из программы\n \nВыберите пункт:")
    manual_engine = int(input())

    if manual_engine == 1:
        start_motor(motor_runing)
    elif manual_engine == 2:
        stop_motor(motor_runing)
    elif manual_engine == 3:
        temperature = int(input("Введите температуру двигателя\n"))
        change_temperature(temperature)
    elif manual_engine == 4:
        show_motor_status(temperature, motor_runing)
    elif manual_engine == 5:
        break
count = +1