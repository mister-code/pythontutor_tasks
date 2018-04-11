'''
Задача «Ход коня»
Условие

Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали,
или наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним ходом.
 '''

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 - 1 == x2 and y1 + 2 == y2:
    print("YES")
elif x1 + 1 == x2 and y1 - 2 == y2:
    print("YES")
elif x1 + 2 == x2 and y1 - 1 == y2:
    print("YES")
elif x1 - 2 == x2 and y1 + 1 == y2:
    print("YES")
elif x1 + 2 == x2 and y1 + 1 == y2:
    print("YES")
elif x1 - 2 == x2 and y1 - 1 == y2:
    print("YES")
else:
    print("NO")
