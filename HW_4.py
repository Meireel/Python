#Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
# Размер списка n ввести с клавиатуры.Найти номер минимального элемента списка.

import random

size=int(input('Размер: \n'))
A=[]

for count in range(0, size):
    A.append(random.randint(0, 99))

i = 0
minIndex = 0
minValue = 100
while i < len(A):
    if A[i] < minValue:
        minIndex = i;
        minValue = A[i]
    i = i + 1

print(minIndex)
