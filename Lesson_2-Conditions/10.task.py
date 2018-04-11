'''
Задача «Ход ферзя»
Условие

Шахматный ферзь ходит по диагонали, горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом.

 '''

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

first_cell = abs(x1 - x2)
second_cell = abs(y1 - y2)

if (x1 == x2 or y1 == y2) or first_cell == second_cell:
    print("YES")
else:
    print("NO")
