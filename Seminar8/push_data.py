from input_data import input_data
from write_data import write_data


def push_data():
    dct = input_data()

    # id;surname;name;class;letter   - name.csv
    write_data([dct.get("id"), dct.get("surname"), dct.get("name"), dct.get("class"), dct.get("letter")], "H:\\Python\\Seminars_Python\\Seminar8\\name.csv")

    # id;city;street;house;apartament;  - class.csv
    write_data([dct["id"], dct["city"], dct["street"], dct["house"], dct["apartament"]], "H:\\Python\\Seminars_Python\\Seminar8\\adress.csv")

    # id;row;col - adress.csv
    write_data([dct["id"], dct["row"], dct["col"]], "H:\\Python\\Seminars_Python\\Seminar8\\class.csv")