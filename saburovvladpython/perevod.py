dictionary = {
    "Hello": "Привет",
    "Hello1": "Привет1",
    "Hello2": "Привет2",
    "Hello3": "Привет3",
    "Hello4": "Привет4",
    "Hello5": "Пока5"
}
zapros = str(input("Введите слово на английском"))
while zapros != "quit":
    if zapros in dictionary:
        print(f"Перевод - {dictionary[zapros]}")
    elif zapros not in dictionary:
        print("Хотите добавить новое слово? Напишите его а затем его перевод")
        newwordeng = str(input())     
        newwordrus = str(input())  
        dictionary[newwordeng] = newwordrus   
    zapros = str(input("Введите слово на английском"))