# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод 
# – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена
# система автоматического сбора черники. Эта система состоит из управляющего
# модуля и нескольких собирающих модулей. Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого 
# куста и с двух соседних с ним. Напишите программу для нахождения
# максимального числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым кустом заданной 
# во входном файле грядки.

import random 
n = int(input('введите количество кустов '))    # ввод кол-ва элементов массива
a = [random.randint(1, 10) for _ in range(n)]   # рандомное значения элементов
print(a)    # вывод массива
b = a[:] + a[:2]    # формирование второго массива с добавлением в конец двух первых элементов
print(b)    # печать нового массива
res = []    # объявление переменной для подсчета суммы трех элементов
max = 0     # объявление максимального значения
for i in range(len(b)-2):   # цикл по подсчету 3-х елементов в списке
    res = sum(b[i:i+3])
    if max < res:   # нахождение максимального
        max = res
        el = b[i:i+3]   # список из 3-х значений дающих максимум
print(max, el) 
    