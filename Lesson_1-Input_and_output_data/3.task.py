'''
Задача «Дележ яблок»
Условие
n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке? Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).  
'''

# Число n можно считать так:
n = int(input())
k = int(input())

rezult = k // n
ost = k % n

# Выводите результат через print()
print(rezult)
print(ost)