# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def inputNumbers(text):
    while True:
        number = input(f'{text}')
        if not number.isdigit():
            print('Нужно ввести целое положительное число!')
        else:
            return int(number)


def primeMultipliers(num):
    result = []
    for i in range(2, num):
        while num % i == 0:
            num /= i
            result.append(i)
    return result

num = inputNumbers("Введите натуральное число N: ")

print(f"Список простых множителей: {primeMultipliers(num)}")