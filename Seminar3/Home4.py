# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def inputNumbers(text):
    while True:
        number = input(f'{text}')
        if not number.isdigit():
            print('Нужно ввести целое положительное число!')
        else:
            return int(number)

num = inputNumbers("Введите натуральное число: ")

decimal_number = num
binary_number = ""
 
while decimal_number > 0:
    binary_number = str(decimal_number % 2) + binary_number
    decimal_number = int(decimal_number / 2)
 
print (f' {num} в двоичной системе -> {binary_number}')