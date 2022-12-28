# Вычислить число c заданной точностью d

# Пример: при d = 0.001, π = 3.141    10⁻¹ ≤ d ≤ 10⁻¹⁰

def inputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Вы вводите не число")
    return number

def getCount(number):
    count = 0
    
    while number % 1 != 0:
        number *= 10
        count += 1
    
    return count

num1 = inputNumbers("Введите 1 число: ")
num2 = inputNumbers("Введите 2 число: ")
d = (inputNumbers("Введите точность d (10⁻¹ ≤ d ≤ 10⁻¹⁰): "))
d = getCount(d)
result = round((num1/num2), d)
print(f"Результат деления c точностью до {d} знаков: {result}")