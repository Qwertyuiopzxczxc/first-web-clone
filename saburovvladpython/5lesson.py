length1 = 5
width1 = 3
area1 = length1 * width1
print(f"Площадь комнаты 1 {area1}")

def great(name):
    """" Эта функция пишем привет """
    print(f"Привет {name} это моя первая функция")

great("Олег")
great("Саня")
great("Никитос")

def introduce(name, age, city):
    """Рассказ о человеке"""
    print(f"Меня зовут {name}, мне {age} лет, я живу в city")

introduce("Олег", 42, "17")
 
def calcuate_area(length, width):
    area = length * width
    return area

room_area = calcuate_area(5, 3)
print(f"Площадь комнаты: {room_area}")

def isAdult(age):
    if age >= 18:
        return True
    else:
        return False
    
if isAdult(20):
    print("Доступ разрешен")
else:
    print("Катись отсюда маленки")


radius = int(input("Введите радиус круга"))



def circle_area(radius):
    area = 3.14 * radius**2
    return area
circle = circle_area(radius) 
print(f"Площадь круга: {circle}")
a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
c = int(input("Введите третье число"))
def max_of_three(a,b,c):
    max = 0
    if a > max:
        max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max
maximum = max_of_three(a, b, c)
print(f"Максимально число: {maximum}")   