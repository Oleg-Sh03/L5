#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
#и возводит число А в целую степень B с помощью рекурсии.
#*Пример:*
#A = 3; B = 5 -> 243 (3⁵)
#    A = 2; B = 3 -> 8 

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
def power(m, n):
    if m == 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return m
    else:
        return m * power (m, n -1)
result = power(a, b)
print(a, "в степени", b, "=", result)