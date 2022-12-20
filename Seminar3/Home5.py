# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def inputNumbers(text):
    while True:
        number = input(f'{text}')
        if not number.isdigit():
            print('Нужно ввести целое положительное число!')
        else:
            return int(number)


def recursion(n):
    if n in (1, 2):
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return ((-1)**(n+1))*recursion(-n)
    else:
        return recursion(n - 1) + recursion(n - 2)

num = inputNumbers("Введите натуральное число: ")
    
fibonacci = []

for i in range(-num, num+1):
    fibonacci.append(int(recursion(i)))
 
print(fibonacci)