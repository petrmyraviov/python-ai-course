workshop_management =[
    {
        "name": "Конвейер",
        "Power": "15 кВт",
        "voltage":" 380 В",
        "frequency": "50 Гц",
        "status": "OFF"
    }
    ,
    {
        "name": "Вытяжка",
        "Power": "7 кВт",
        "voltage":" 380 В",
        "frequency": "50 Гц",
        "status": "OFF"
    }
]

start = 0
def interface(): # Функция интерфейса
    print("\n===============================\n")
    print("Пульт управления цехом")
    print("\n===============================\n")
    print("1. Показать оборудование")
    print("2. Включить двигатель")
    print("3. Выключить двигатель")
    print("4. Добавить двигатель")
    print("5. Удалить двигатель")
    print("6. Изменить напряжение")
    print("7. Найти двигатель")
    print("8. Статистика")
    print("9. Выход\n")
    print("Выберите пункт:")

def show_equipment(workshop_management): # Функция отображения оборудования
    print("Оборудования цеха")
    for workshop_managements in (workshop_management):
        for for_workchop in workshop_managements:
            print(for_workchop, ":", workshop_managements[for_workchop], end="\n")

def on_switch_motor(workshop_management): # Функция включения двигателя
    print("Название двигателя для включения")
    name_motors = input().strip()
    for workshop_managements in (workshop_management):
        if workshop_managements.get("name") == name_motors and workshop_managements.get("status") == "OFF":
            workshop_managements["status"] = "ON"
            print(f"Двигатель {name_motors} включен")
            break
        elif workshop_managements.get("status") == "ON" and workshop_managements.get("name") == name_motors:
            print(f"Двигатель {name_motors} уже включен")
            break
        elif workshop_managements.get("name") != name_motors:
            continue
    else:
        print("Двигатель не найден")
    return None

def off_switch_motor(workshop_management): # Функция выключения двигателя
    print("Название двигателя для выключения")
    name_motors = input().strip()
    for workshop_managements in (workshop_management):
        if workshop_managements.get("name") == name_motors and workshop_managements.get("status") == "ON":
            workshop_managements["status"] = "OFF"
            print(f"Двигатель {name_motors} выключен")
            break
        elif workshop_managements.get("status") == "OFF" and workshop_managements.get("name") == name_motors:
            print(f"Двигатель {name_motors} уже выключен")
            break
        elif workshop_managements.get("name") != name_motors:
            continue
    else:
        print("Двигатель не найден")
    return None   
    
def add_motor(workshop_management): # Функция добавления двигателя
    print("Введите название двигателя")
    name_motors = input().strip()
    print("Введите мощность двигателя")
    power_motors = input().strip()
    print("Введите напряжение двигателя")
    voltage_motors = input().strip()
    print("Введите частоту двигателя")
    frequency_motors = input().strip()
    new_motor = {
        "name": name_motors,
        "Power": power_motors,
        "voltage": voltage_motors,
        "frequency": frequency_motors,
        "status": "OFF"
    }
    workshop_management.append(new_motor)
    print(f"Двигатель {name_motors} добавлен в список оборудования")

def remove_motor(workshop_management): # Функция удаления двигателя
    print("Введите название двигателя для удаления")
    name_motors = input().strip()
    for workshop_managements in (workshop_management):
        if workshop_managements.get("name") == name_motors:
            workshop_management.remove(workshop_managements)
            print(f"Двигатель {name_motors} удален из списка оборудования")
            break
    else:
        print("Двигатель не найден")

def change_voltage(workshop_management): # Функция изменения напряжения двигателя
    print("Введите название двигателя для изменения напряжения")
    name_motors = input().strip()
    for workshop_managements in (workshop_management):
        if workshop_managements.get("name") == name_motors:
            print(f"Текущее напряжение двигателя {name_motors}: {workshop_managements.get('voltage')}")
            print("Введите новое напряжение двигателя")
            new_voltage = input().strip()
            workshop_managements["voltage"] = new_voltage
            print(f"Напряжение двигателя {name_motors} изменено на {new_voltage}")
            break
    else:
        print("Двигатель не найден")


def find_motor(workshop_management): # Функция поиска двигателя
    print("Введите название двигателя для поиска")
    name_motors = input().strip()
    for workshop_managements in (workshop_management):
        if workshop_managements.get("name") == name_motors:
            print(f"Двигатель {name_motors} найден в списке оборудования")
            print(f"Мощность: {workshop_managements.get('Power')}")
            print(f"Напряжение: {workshop_managements.get('voltage')}")
            print(f"Частота: {workshop_managements.get('frequency')}")
            print(f"Статус: {workshop_managements.get('status')}")
            break
    else:
        print("Двигатель не найден")

    
def statistics(workshop_management): # Функция статистики
    total_motors = len(workshop_management)
    on_motors = sum(1 for motor in workshop_management if motor.get("status") == "ON")
    off_motors = total_motors - on_motors
    print(f"Общее количество двигателей: {total_motors}")
    print(f"Количество включенных двигателей: {on_motors}")
    print(f"Количество выключенных двигателей: {off_motors}")

while True: # Основной цикл программы
    interface()
    start = input() # Выбор пункта меню
    if not start.isdigit(): # Проверка на ввод числа
        print("Вы ввели не число, попробуйте снова") # Сообщение об ошибке
    elif int(start)  <= 9 and int(start) >= 1: # Проверка на ввод числа от 1 до 9
        match int(start):
            case 1: # Показать оборудование
                show_equipment(workshop_management)
            case 2: # Включить двигатель
                on_switch_motor(workshop_management)
            case 3: # Выключить двигатель
                off_switch_motor(workshop_management)
            case 4: # Добавить двигатель
                add_motor(workshop_management)
            case 5: # Удалить двигатель
                remove_motor(workshop_management)
            case 6: # Изменить напряжение
                change_voltage(workshop_management)
            case 7: # Найти двигатель
                find_motor(workshop_management)
            case 8: # Статистика
                statistics(workshop_management)
            case 9: # Выход
                print("Выход")
                break
    else: # Проверка на ввод числа больше 8
            print("Вы ввели не верное число, попробуйте снова")


