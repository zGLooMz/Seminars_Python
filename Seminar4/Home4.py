# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def inputNumbers(text):
    while True:
        number = input(f'{text}')
        if not number.isdigit():
            print('Нужно ввести целое положительное число!')
        else:
            return int(number)

def writeFile(st):
    with open('H:\Python\Seminars_Python\Seminar4\Home4.txt', 'w') as data:
        data.write(st)


max_koef=100
k = inputNumbers("Введите натуральное число k: ")

koeff=[randint(0,max_koef) for i in range(k)]+[randint(0,max_koef)]
polynomial='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])

polynomial=polynomial.replace('x^1+', 'x+')
polynomial=polynomial.replace('x^0', '')
polynomial+=('','1')[polynomial[-1]=='+']
polynomial=(polynomial, polynomial[:-2])[polynomial[-2:]=='^1'] + '=0'
print(polynomial)
writeFile(polynomial)
