'''
Задача «Сколько совпадает чисел»
Условие
Даны три целых числа. Определите, сколько среди них совпадающих.
Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны). 
 '''

number = []

for i in range(3):
    number.append(input())

if number[0] == number[1] == number[2]:
    print(3)
elif number[0] == number[1] or number[1] == number[2] or number[0] == number[2]:
    print(2)
else:
    print(0)

