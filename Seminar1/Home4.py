# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def inputNumbers(inputText):
    while True:
        number = input(f'{inputText}')
        if not number.isdigit() or not 0 <= int(number) <=4:
            print('Нужно ввести целое число от 1 до 4')
        else:
            return int(number)

quarter = inputNumbers('Введите номер четверти: ')

if quarter == 1:
    print('Возможные координаты x(0;+∞) и y(0;+∞)')
elif quarter == 2:
    print('Возможные координаты x(0;-∞) и y(0;+∞)')
elif quarter == 3:
    print('Возможные координаты x(0;-∞) и y(0;-∞)')
else:
    print('Возможные координаты x(0;+∞) и y(0;-∞)')