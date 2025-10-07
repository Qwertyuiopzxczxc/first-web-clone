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