'''
Задача «Ход слона»
Условие

Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите,
может ли слон попасть с первой клетки на вторую одним ходом.

 '''

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

first_cell = abs(x1 - x2)
second_cell = abs(y1 - y2)

if first_cell == second_cell:
    print("YES")
else:
    print("NO")
