workshop_management = {
    "name": "Ковейер",
    "Power": "15 кВт",
    "voltage":" 380 В",
    "frequency": "50 Гц",
    "status": "OFF"
}

start = 0
def interface():
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
while True:
    interface()
    start = int(input())
    if int(start):
        match start:
            case 1:
                print("Оборудования цеха")
                for workshop_managements in (workshop_management):
                    print(workshop_managements, workshop_management[workshop_managements])
            case 2:
                workshop_management["status"] = "ON"
            case 3:
                workshop_management["status"] = "OFF"
            case 4:
                motor = {
                    "name": "Ковейер",
                    "Power": "15 кВт",
                    "voltage":" 380 В",
                    "frequency": "50 Гц",
                    "status": "OFF"
                }
            case 5:
                print("Удалить двигатель")
            case 6:
                print("Изменить напряжение")
            case 7:
                print("Найти двигатель")
            case 8:
                print("Статистика")    
            case 0:
                print("Выход")
                break
      

