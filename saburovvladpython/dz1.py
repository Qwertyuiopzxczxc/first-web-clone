n1 = int(input('Кол-во монет по 5 рублей')) * 5
n2 = int(input('Кол-во монет по 10 рублей')) * 10
age = int(input('Твой возраст'))
name = str(input('Ваше имя'))
sabaka = 20
if (age % 2 == 0 and age >= 18 and name != "олег" and name != "Олег"):
    print('Вам продадут - ', (n1 + n2) / sabaka, 'Хот Догов')
elif(name == 'олег' or name == 'Олег'):
    print('Вы в черном списке!')
elif (age < 18):
    print('Тебе нету 18!')
elif (age % 2 == 1):
    print('У вас нечетный возраст!')


