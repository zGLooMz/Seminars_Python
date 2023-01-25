# модуль

def import_data(data, sep=None):
    with open('H:\Python\Seminars_Python\Seminar7\phone.csv', 'a+') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")