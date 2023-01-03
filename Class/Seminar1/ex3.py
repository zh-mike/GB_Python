# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

from random import randint
'''
N = int(input("-> "))
list_N =[]
76y6
for i in range(-N, N+1):
    list_N.append(i)

print(list_N)
'''
N = int(input("-> "))

for i in range(-N, N+1):
    print(f'{i}', end=" ")
