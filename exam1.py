
motor_running = False 
temperature = 25
count = 6
# Визуальное отоброжения линии меню
def image_manual():
    print("=============================")
# Запуск двигателя 
def start_motor(motor_running):
    if  motor_running == False:
        motor_running = True
        print("Двигатель запущен")
        return motor_running
    else:
        print("Двигатель уже работает")
        return motor_running    
    
# Остановка двигателя
def stop_motor(motor_running):
    if  motor_running == True:
        motor_running = False
        print("Двигатель остановлен")
        return motor_running
    else:
        print("Двигатель уже остановлен")
        return motor_running
    
# Статус двигателя его состояния в работе 
def show_motor_status(temperature, motor_running):
    image_manual()
    print("Состояние двигателя:\n")
    if motor_running == True:
        print("Двигатель работает\n")
        print(f"Температура двигателя: {temperature}°C\n")
        image_manual()
    else:
        print("Двигатель остановлен\n")
        print(f"Температура двигателя: {temperature}°C\n")
        image_manual()

# Температура двигателя 
def change_temperature(temperature):
        image_manual()
        print(f"\nТемпература двигателя: {temperature}°C\n")
        image_manual()
        return temperature

# Цикл запуска программы 
while count >1:
    image_manual()
    print("    УПРАВЛЕНИЕ ДВИГАТЕЛЕМ")
    image_manual()

    print("\n1. Запустите двигатель\n \n2. Остановите двигатель\n \n3. Измерте температуру двигателя\n \n4. Показать состояние двигателя\n \n5. Выйти из программы\n \nВыберите пункт:")
    manual_engine = int(input())

    if manual_engine == 1 and temperature >= 80:
        print("Запуск невозможен.\n двигатель перегрет.\n")
    elif manual_engine == 1 and temperature <= 79:
        motor_running = start_motor(motor_running)
    elif motor_running == True and temperature >= 80:
        motor_running = False
        print("Экстренная остановка двигателя, перегрев двигателя")
    elif manual_engine == 2:
        motor_running = stop_motor(motor_running)
    elif manual_engine == 3:
        temperature = int(input("Введите температуру двигателя\n"))
        temperature = change_temperature(temperature)
    elif manual_engine == 4:
        show_motor_status(temperature, motor_running)
    elif manual_engine == 5:
        break
count = +1