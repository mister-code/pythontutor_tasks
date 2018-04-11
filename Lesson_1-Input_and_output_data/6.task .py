'''
Задача «Следующее и предыдущее»
Условие
Напишите программу, которая считывает целое число и выводит текст,
аналогичный приведенному в примере (пробелы важны!). 
 '''

number = int(input())

print("The next number for the number {} is {}.".format(number, number+1))
print("The previous number for the number {} is {}.".format(number, number-1))
