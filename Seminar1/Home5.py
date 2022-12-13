# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def inputNumbers(x):
    xy = ["x", "y"]
    coord = []
    for i in range(x):
        while True:
            number = input(f'Введите значение {xy[i]}: ')
            if number.isalpha():
                print('Нужно ввести число!')
            else:
                coord.append(float(number))
                break
    return coord

def distanceBetweenPoints(a, b):
    distance = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return distance

print('Введите координаты точки А')
point_a = inputNumbers(2)
print('Введите координаты точки В')
point_b = inputNumbers(2)

result = distanceBetweenPoints(point_a, point_b)

print(f'Расстояние между точками: {format(result, ".2f")}')