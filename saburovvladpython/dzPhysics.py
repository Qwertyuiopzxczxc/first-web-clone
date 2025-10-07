import math
g = 10
height = int(input("Введите высоту падения в метрах"))
fall_time = math.sqrt((2*height) / g)
print(f"Время падения составит {fall_time} секунд")
