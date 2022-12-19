# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def InputNumbers(text):
    flag = False
    while not flag:
        try:
            number = float(input(f"{text}"))
            flag = True
        except ValueError:
            print("Нужно ввести число")
    return number


def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")