
motor_runing = False 
temperature = 25
count = 6
# Визуальное отброжения линии меню
def imagel_manual():
    print("=============================")
# Запуск двигателя 
def start_motor(motor_runing):
    if  motor_runing == False:
        motor_runing = True
        print("Двигатель запущен")
        return motor_runing
    else:
        print("Двигатель уже работает")
        return motor_runing    
    
# Остоновка двигателя
def stop_motor(motor_runing):
    if  motor_runing == True:
        motor_runing = False
        print("Двигатель остановлен")
        return motor_runing
    else:
        print("Двигатель уже остановлен")
        return motor_runing
    
# Статус двигателя его состояния в работе 
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

# Температура двигателя 
def change_temperature(temperature):
        imagel_manual()
        print(f"\nТемпература двигателя: {temperature}°C\n")
        imagel_manual()
        return temperature

# Цикл запуска программы 
while count >1:
    imagel_manual()
    print("    УПРАВЛЕНИЕ ДВИГАТЕЛЕМ")
    imagel_manual()

    print("\n1. Запустите двигатель\n \n2. Остановите двигатель\n \n3. Измерте температуру двигателя\n \n4. Показать состояние двигателя\n \n5. Выйти из программы\n \nВыберите пункт:")
    manual_engine = int(input())

    if manual_engine == 1 and temperature >= 80:
        print("Запуск невозможен.\n двигатель перегрет.\n")
    elif manual_engine == 1 and temperature <= 79:
        motor_runing = start_motor(motor_runing)
    elif motor_runing == True and temperature >= 80:
        motor_runing = False
        print("Экстриная остоновка двигателя, перегрев двигателя")
    elif manual_engine == 2:
        motor_runing = stop_motor(motor_runing)
    elif manual_engine == 3:
        temperature = int(input("Введите температуру двигателя\n"))
        temperature = change_temperature(temperature)
    elif manual_engine == 4:
        print(motor_runing)
        show_motor_status(temperature, motor_runing)
    elif manual_engine == 5:
        break
count = +1