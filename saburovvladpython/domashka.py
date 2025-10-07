max = 0
sumaRashodov = 0
rashod = []
for i in range(7):
    babki = int(input("Введите сумму расходов"))
    rashod.append(babki)
    sumaRashodov = sumaRashodov + babki
    if babki > max:
        max = babki

print(sumaRashodov, "Потратил бабок")
print(sumaRashodov / i, "В среднем потратил бабок")
print(max, "Максимально потратил бабок")