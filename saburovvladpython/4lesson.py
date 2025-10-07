book = {
    "title": "1984",
    "author": "Джордж Оруэлл",
    "year": 1948,
    "genre": "Антиутопия"
}

player = {
    "name": "Oleg67",
    "damage": 20.3,
    "id": 1,
    "age": 52,
    "city": 17,
    "isAlive": True
}

simple = {
    1: "Один",
    2: "Да"
}

print(player["name"])

print(player.get("city"))
print(player.get("class")) # none (Без ошибки)
print(player.get("class", "Не найден"))

# Перезаписать элемент в ключе damage
player["damage"] = 22.5
# Создастся новая пара ключ значение
player["class"] = "калдун"

print(player)

# Если внутри словаря player есть ключ name, то выполнить
if "name" in player: 
    print("Ключ name существует!")

if "HP" not in player:
    print("Ключ HP не найден!")

# Удаление по ключу с возвратом значения
removed_value = player.pop("city")
# Удалить последний элемент списка
last_item = player.popitem()
print("Удалили последнюю пару", last_item)

print(player.keys()) #dict_keys([name, damage, age, isAlive])
print(player.values())
print(player.items())

# Перебор словарей в циклах
# Перебор ключей словаря
for key in player.keys():
    print(key) # Напечатает: name, age, damage ....

# Перебор по значениям
for value in player.values():
    print(value) # Напечатает: Oleg67, 52, 22.5 ......

for key, value in player.items():
    print(f"Ключ {key}, Значение {value}")


# Список словарей.
students = [
    {"name": "Никитос", "age": 0, "grades": [5,4,3,2,1,4]},
    {"name": "Ваня", "age": 87, "grades": [5,5,5,5,5,1]},
    {"name": "Саня", "age": 9, "grades": [3,3,2,4,5,4]}
]

# Получение возраста первого студента
print(students[0]["age"])
print(students[1]["name"])
# Вывод всех имен студентов
for student in students:
    print(student["name"])




dictionary = [
    {"engword": "Hello", "rusword": "Привет"},
    {"engword": "Hello1", "rusword": "Привет1"},
    {"engword": "Hello2", "rusword": "Привет2"},
    {"engword": "Hello3", "rusword": "Привет3"},
    {"engword": "Hello4", "rusword": "Привет4"}
]
zapros = str(input("Введите слово на английском"))
while zapros != "quit":
    if dictionary[1]["engword"] in zapros:
        print(dictionary[1]["rusword"])
    zapros = str(input("Введите слово на английском"))
        