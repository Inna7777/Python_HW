#Задача 2: Найдите сумму цифр трехзначного числа.
print ("Введите трехзначное число")
n = int(input())
sum = 0
while n > 0:
    sum += n % 10
    n = n // 10
print("сумма чисел =", sum)
