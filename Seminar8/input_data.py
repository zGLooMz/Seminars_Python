from write_data import count_data

def input_data():
    dct = dict()
    Id = count_data("H:\\Python\\Seminars_Python\\Seminar8\\name.csv") 
    dct["id"] = Id   
    dct["surname"] = input('Введите Фамилию: ')
    dct["name"] = input('Введите Имя: ')
    dct["class"] = input('Введите Класс: ')
    dct["letter"] = input('Введите Литера: ')
    dct["row"] = input('Введите Ряд: ')
    dct["col"] = input('Введите Номер парты: ')
    dct["city"] = input('Введите Город: ')
    dct["street"] = input('Введите Улица: ')
    dct["house"] = input('Введите Дом: ')
    dct["apartament"] = input('Введите Квартира: ')
    return dct