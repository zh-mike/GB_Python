# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# Пример:
    # n = 3
    #[-3, -2, -1, 0, 1, 2, 3]
    #--> 0 2 3
    #-3 * -1 * 0 = 0
    #Вывод: 0

from random import randint
n = int(input("-> "))
list_num = []

for i in range(n+2):
    list_num.append(randint(-n, n))
print(list_num)

search = input("Введите адрес символа через пробел: ")
sum = list_num[int(search.split(" ")[0])]
length = len(search)

if len(search)%2 == 0:
    length += 1

for j in range(2,length, 2):
    sum *= list_num[int(search[j])]

print(sum)
