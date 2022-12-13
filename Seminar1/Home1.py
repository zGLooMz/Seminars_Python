# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

def inputNumbers(inputText):
    while True:
        number = input(f'{inputText}')
        if not number.isdigit():
            print('Нужно ввести целое число!')
        else:
            return int(number)

def checkNumber(number):
    if 6 <= number <= 7:
        print('Да, это выходной')
    elif 0 < number < 6:
        print('Нет, это не выходной')
    else:
        print('Число не обозначает день недели!')


num = inputNumbers('Введите число: ')
checkNumber(num)