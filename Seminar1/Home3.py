# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def inputСoord(x):
    coord = [0] * x
    for i in range(x):
        while True:
            number = input(f'Введите {i+1} координату: ')           
            if number.isalpha():
                print('Нужно ввести число!')
            elif float(number) == 0:
                print('Координата не должно быть равна 0 ')
            else:
                coord[i] = float(number)
                break    
    return coord

def checkCoordinates(xy):
    quarter = 1
    if xy[0] < 0 and xy[1] > 0:
        quarter = 2
    elif xy[0] < 0 and xy[1] < 0:
        quarter = 3
    elif xy[0] > 0 and xy[1] < 0:
        quarter = 4
    print(f'Точка находится в {quarter} четверти плоскости')

сoordinate = inputСoord(2)
checkCoordinates(сoordinate)