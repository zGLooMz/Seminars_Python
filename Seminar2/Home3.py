#  Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# *Пример:*

# - Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма = 9.06

def InputNumbers(text):
    while True:
        number = input(f'{text}')
        if not number.isdigit():
            print('Нужно ввести целое положительное число!')
        else:
            return int(number)

num = InputNumbers("Введите число: ")

my_list = []

for i in range(1, num+1):
    n = (1+1/i)**i
    my_list.append(round(n, 2))
    
summ = 0
for j in range(len(my_list)):
    summ = summ + my_list[j]

print(my_list)
print(f'Сумма = {round(summ, 2)}')
