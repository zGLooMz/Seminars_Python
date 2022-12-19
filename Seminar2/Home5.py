# Реализуйте алгоритм перемешивания списка.

import random

def InputNumbers(text):
    while True:
        number = input(f'{text}')
        if not number.isdigit():
            print('Нужно ввести целое положительное число!')
        else:
            return int(number)

num = InputNumbers("Введите число: ")

array = [random.randint(0, num) for i in range (0,num)]
print(array)

new_array = array
new_array_length = len(new_array)
for i in range(new_array_length):
    index = random.randint(0, new_array_length - 1)  
    temp = new_array[i]
    new_array[i] = new_array[index]
    new_array[index] = temp
print(new_array)