from read_data import read_data


def init():
    if not (len(read_data()) > 0):
        
        with open("H:\\Python\\Seminars_Python\\Seminar8\\name.csv", 'a+') as file:
            file.write("id;surname;name;class;letter\n")

        with open("H:\\Python\\Seminars_Python\\Seminar8\\adress.csv", 'a+') as file:
            file.write("id;city;street;house;apartament;\n")

        with open("H:\\Python\\Seminars_Python\\Seminar8\\class.csv", 'a+') as file:
            file.write("id;row;col\n")