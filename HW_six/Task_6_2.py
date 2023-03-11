# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
my_lst = [random.randint(-100, 100) for _ in range(10)]
print(my_lst)
my_lst2 =[]
for i, value in enumerate(my_lst):
    if 0 < value < 100:
        my_lst2.append(i)
print(my_lst2)

