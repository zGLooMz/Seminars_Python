# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 

def InputNumbers(text):
    while True:
        number = input(f'{text}')
        if not number.isdigit():
            print('Нужно ввести целое положительное число!')
        else:
            return int(number)

num = InputNumbers("Введите число: ")

import random
my_array = [random.randint(-num, num) for i in range (0,num)]
print(my_array)
find_num1 = InputNumbers("Введите индекс первого элемеента: ")
find_num2 = InputNumbers("Введите индекс второго элемеента: ")

print (f'Произведение элементов на указаных позициях = {my_array[find_num1]*my_array[find_num2]}')