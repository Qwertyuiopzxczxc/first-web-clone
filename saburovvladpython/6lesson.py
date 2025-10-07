# Открытие файла для чтения
# open("что за файл надо открыть", "что с ним сделать?", "кодировка") - открыть и сохранить файл
file = open("sxt.txt", "r", encoding="utf-8")
# read() - прочесть содержимое
content = file.read()
# файл важно закрыть после чтения
file.close()
print(content)

# Безопасное чтение файла с последующим закрытием
with open("sxt.txt", "r", encoding="utf8") as file:
    content = file.read()
    print("Весь файл\n")
    print(content)
# Файл гарантировано закроется после выхода из блока with

# "r" - чтение read (по умолчанию)
# "w" - запись write (перезаписывает файл)
# "a" - добавление в конец файла
# "r+" - чтение и запись 
# Режим "w" - перезапись файла (если файл существует - перезапишется, если его нет, создаст)
# /n - спец. символ для отступа на след. строку. Имимтация Enter
# .write() - запись строки в файл
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Привет, это мое первое изменение файла\n")
    file.write("А это моя вторая записанная строка\n")

# Режим "a" - добавление в конец файла 
with open("output.txt", "a", encoding="utf-8") as file:
    file.write("А это моя 3 строка, я добавил ее позже")
with open("output.txt", "r", encoding="utf8") as file:
    content = file.read()

# Методы чтения файлов
with open("example.txt", "r", encoding="utf8") as file:
    # read() -  читает файл, как одну строку
    content = file.read()
    print("Весь файл:")
    print(content)

# Чтение только одной строки
with open("example.txt", "r", encoding="utf8") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"Первая строка, {line1}")
    print(f"Первая строка, {line2}")
with open("numbers.txt", "r", encoding="utf8") as file:
    #readlines() - читает все строки, как элементы списка
    lines = file.readlines()
    print("Все строки, как список:")
    zero = 0
    for line in lines:
        c = print(line.strip()) # strip() убирает лишние пробелы и переносы строк
    for i in range(10):
        suma = file.readlines()
        map = map(int, suma)

print(map)




