# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def InputNumbers(text):
    flag = False
    while not flag:
        try:
            number = int(input(f"{text}"))
            flag = True
        except ValueError:
            print("Нужно ввести целое число")
    return number

def recursion(n):
    if n == 1:
        return 1
    else:
        return n * recursion(n - 1)

num = InputNumbers("Введите число: ")

recursion_list = []
for j in range(1, num + 1):
    recursion_list.append(recursion(j))

print(f"При N = {num}:  {recursion_list}")