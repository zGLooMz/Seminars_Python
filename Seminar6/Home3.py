# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def inputNumbers(text):
    while True:
        number = input(f'{text}')
        if not number.isdigit():
            print('Нужно ввести целое положительное число!')
        else:
            return int(number)

num = inputNumbers("Введите число (количество элементов в списке): ")

lst = [(-3)**i for i in range(num)]
print(f"Итоговая последовательность после применения list comprehension: {lst}")