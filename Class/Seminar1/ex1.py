# Узнаем является ли одно число квадратом другого

a = int(input("Number1: "))
b = int(input("Number2: "))

if b == a**2:
    print("Да")
elif a == b**25:
    print("Да")
else:
    print("Нет")

#ansver = print("Да") if b**2 else print("Нет") однострочное решение но без elif