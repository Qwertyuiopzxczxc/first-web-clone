empty_list = []

fruits = ["apple", "banana", "Watermelon"]

mixed_list = [1, "Hello", 3.14, True]

numbers = list([1,2,3,4,5])

print(fruits[2])

print(fruits[-1])

print(fruits)

fruits.append("Pineapple")

print(fruits)

fruits.insert(1, "kiwi")

print(fruits)

names = ["Ilya", "Danya", "Olga", "Sanya", "Masha", "Vanya", "Andrey", "Jora", "Roma", "Vitalya", "Yura"]

names.insert(2, "Oleg")
names.insert(4, "Oleg")
names.insert(10, "Oleg")
names.append("Inokentiy")
print(names)

fruits.remove("kiwi")

print(fruits)

pop_result = fruits.pop(-1)

print("Удален", pop_result)

print(fruits)

numbers = [0,1,2,3,4,5,6,7,8,9]

# От 2 до 4
print(numbers[2:5])
# От начала до 4
print(numbers[:5])
# От 5 до конца списка
print(numbers[5:])
# Вывод всего списка, но через 1 элемент
print(numbers[::2])
# Вывод всего списка в обртаном порядке
print(numbers[::-1])

for fruit in fruits:
    print("я люблю ", fruit)

list_length = len(fruits)
print(list_length)

for i in range(len(fruits)):
    print("Элемент под индексом", i, "это", fruits[i])

prices = [100, 250, 300, 50]

total = 0
max = 10
sumaRashodov = 0
for price in prices:
    total = total + price
print("Сумма всех цен", total)

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