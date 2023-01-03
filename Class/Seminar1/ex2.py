#Найти максимум из списка

list_a = [ 1, 4, 8, 7, 5 ]
maxx = list_a[0]
for _ in range(len(list_a)):
    if maxx < list_a[_]:
        maxx = list_a[_]
print(maxx)

'''

numbers = []
for _ in range(1, 5):
numbers.append(int(input('--> ')))
max_count = max(numbers)
print(numbers)
print(max_count)
'''