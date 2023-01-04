# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

'''
my_string = "Я люблю Python"
start = -1
count = 0
x = input("->")
while True:
    start = my_string.find(x, start+1)
    if start == -1:
        break
    count += 1

print("Количество вхождений символа в строку: ", count )
'''
string = "Привееет"
search = "е"
print(string.count(search))
