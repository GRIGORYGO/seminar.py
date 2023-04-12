"""
Задача No9. Решение в группах
По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
Решить задачу используя цикл while
Input: 5
Output: 120
"""

x = int(input("Введите число: "))
factorial = 1
a = 1
while a <= x:
    factorial = factorial * a
    a = a + 1
else:   
    print(factorial)
