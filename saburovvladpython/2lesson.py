a = 1
b = 5

a + b
a - b
a * b
a / b
a % b

a = int(input('Введите целое число'))
if (a == 0):
    print('Число - 0')
elif (a % 2 == 1):
    print('Число не четное')
elif (a % 2 == 0):
    print("Число четное")