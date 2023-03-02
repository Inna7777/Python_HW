# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X.
import random
N = int(input('Введите размер массива '))
lst = [random.randint(0,10) for _ in range(N)]
print(lst)
x = int(input('введите число'))
min = lst[0]
for i in lst:
    if abs(i - x) < abs(min - x):
        min = i
print(min)