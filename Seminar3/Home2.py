# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
def inputNumbers(text):
    while True:
        number = input(f'{text}')
        if not number.isdigit():
            print('Нужно ввести целое положительное число!')
        else:
            return int(number)

num = inputNumbers("Введите число (количество элементов в списке): ")

my_array = [random.randint(0, num+5) for i in range (0,num)]
print(my_array)

new_array = []

for i in range(len(my_array)):
    if i > len(my_array)-1-i:
       break
    n = my_array[i]*my_array[len(my_array)-1-i]
    new_array.append(n)

print(new_array)