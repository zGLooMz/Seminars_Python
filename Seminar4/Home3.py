# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

import random


def inputNumbers(text):
    while True:
        number = input(f'{text}')
        if not number.isdigit():
            print('Нужно ввести целое положительное число!')
        else:
            return int(number)

def uniqueNumbers(numbers):
    unique = []
    for i in numbers:
        if i not in unique:
            unique.append(i)
    return unique

num = inputNumbers("Введите число (количество элементов в списке): ")

my_array = [random.randint(0, num) for i in range (0,num)]

print(my_array)
print(uniqueNumbers(my_array))

