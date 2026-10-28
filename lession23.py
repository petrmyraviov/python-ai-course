# заданя 23.1
motors  = [
    {"name": "Конвейер"}, {"name": "Вытяжка"}
    ]
backup_motors = motors.copy() # Создай копию списка motors и присвой её переменной backup_motors.
backup_motors.append({"name": "Насос"}) # Добавь в список backup_motors словарь с именем "Насос".
print("motors:""\n", motors) # Выведи список motors на экран.
print("backup_motors:""\n", backup_motors) # Выведи список backup_motors на экран.
# заданя 23.2
motors = [
    {"name": "Конвейер", "status": "OFF"},
    {"name": "Вытяжка", "status": "ON"}
]

backup = motors.copy()
backup[0]["status"] = "ON" # Измени статус первого мотора в списке backup на "ON".
backup = [{"name": "Насос", "status": "OFF"}] # Создай новый список backup, который будет содержать словарь с именем "Насос" и статусом "OFF".
print("motors:""\n", motors) # Выведи список motors на экран.
print("backup:""\n", backup) # Выведи список backup на экран.

# заданя 23.3
from copy import deepcopy # Импортируй функцию deepcopy из модуля copy.
motors = [
    {"name": "Конвейер", "status": "OFF"},
    {"name": "Вытяжка", "status": "ON"}
]
backup = deepcopy(motors)   # Создай глубокую копию списка motors и присвой её переменной backup.
print("motors:""\n", motors) # Выведи список motors на экран.
backup[0]["status"] = "ON" # Измени статус первого мотора в списке backup на "ON".
backup = [{"name": "Насос", "status": "OFF"}] # Соз