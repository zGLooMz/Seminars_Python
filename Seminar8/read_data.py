 

def read_data():
    lst_name = []
    with open('H:\\Python\\Seminars_Python\\Seminar8\\name.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_name.append(temp)
        
    lst_adress = []
    with open('H:\\Python\\Seminars_Python\\Seminar8\\adress.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_adress.append(temp)
        

    lst_class = []
    with open('H:\\Python\\Seminars_Python\\Seminar8\\class.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_class.append(temp)
        

    lst = []
    for i in range(len(lst_name)):
        lst.append([lst_name[i][0], lst_name[i][1], lst_name[i][2], lst_name[i][3], lst_name[i][4], \
            lst_class[i][1], lst_class[i][2], \
            lst_adress[i][1], lst_adress[i][2], lst_adress[i][3], lst_adress[i][4]])
    return lst
