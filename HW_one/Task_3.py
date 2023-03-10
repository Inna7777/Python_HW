# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

print('Введите шестизначное число')
a = int(input())
n = a % 1000
m = a // 1000
sum1 = 0
sum2 = 0
while n > 0 and m > 0:
    
    sum1 += n % 10    
    n //= 10
    sum2+= m % 10
    m //= 10
if sum1 == sum2:
    print('Билет счастливый')
else:
    print('Билет несчастливый')