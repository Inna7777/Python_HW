# Задача 16: Требуется вычислить,
# сколько раз встречается некоторое число X в массиве A[1..N].
N = int(input('Введите размер массива '))
import random
lst = [random.randint(0, 10) for _ in range(N)]
print(lst)
a = int(input('введите число '))
print('число', a , 'встречается ', lst.count(a),'раза')
