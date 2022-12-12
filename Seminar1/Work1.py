# Задачи:

# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

#     *Примеры:*

#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет
# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# first_user_number = int(input(' Enter first number: '))
# second_user_number = int(input(' Enter second number: '))
# print(f'{first_user_number}, {second_user_number} ->', end=' ')

# if first_user_number == second_user_number ** 2 or second_user_number == first_user_number ** 2:
#     print('yes')
# else:
#     print('no')


# numbers = []
# for i in range(1, 6):
#     numbers.append(int(input(f'Введите элемент под номером {i}: ')))
# print(numbers)
# print(max(numbers))


# num = int(input())
# for i in range(-num, num + 1):
#     print(f'{i}, ', end=' ')

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#     *Примеры:*

#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# num = input('Введите дробное число: ')
# if num.isdigit():
#     print('нет')
# else:
#     num = int(float(num)*10 % 10)
#     print(num)

# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.


user_number = int(input('Enter your number: '))

if (user_number % 5 == 0 and user_number % 10 == 0 or user_number % 15 == 0) and user_number%30 != 0:
    print('Your number is nice!')
else:
    print('Try again')
