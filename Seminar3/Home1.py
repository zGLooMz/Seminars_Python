# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
def inputNumbers(text):
    while True:
        number = input(f'{text}')
        if not number.isdigit():
            print('Нужно ввести целое положительное число!')
        else:
            return int(number)

num = inputNumbers("Введите число (количество элементов в списке): ")

my_array = [random.randint(0, num+10) for i in range (0,num)]
print(my_array)
summ = 0
for i in range(len(my_array)):
    if i%2 != 0:
        summ += my_array[i]

print(f'Сумма элементов на нечетных позициях = {summ}')