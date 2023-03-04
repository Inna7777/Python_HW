# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('введите кол-во элементов первого множества '))
set_1 = set()
m = int(input('введите кол-во элементов второго множества '))
set_2 = set()
for i in range(n):
    a = int(input('введите элемент 1-го множества '))
    set_1.add(a) # формируем 1-е множество
print('set_1=', set_1)

for i in range(m):
    b = int(input('введите элемент 2-го множества '))
    set_2.add(b) # формируем второе множество
print('set_2=', set_2)
list_1 = list(set_1.union(set_2)) # складываем два множества
print(list_1)
list_1.sort() # сортируем множество по возрастанию
print(list_1)

