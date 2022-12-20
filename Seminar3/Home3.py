# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
def inputNumbers(text):
    while True:
        number = input(f'{text}')
        if not number.isdigit():
            print('Нужно ввести целое положительное число!')
        else:
            return int(number)

num = inputNumbers("Введите число (количество элементов в списке): ")
my_array=[round(random.uniform(0, 10), 2) for i in range(0, num)]
print(my_array)

new_array = []
for i in range(len(my_array)):
    new_array.append(round(my_array[i]%1, 2))

difference = max(new_array) - min(new_array)
print(f'Разницу между максимальным и минимальным значением дробной части элементов = {round(difference, 2)}')
