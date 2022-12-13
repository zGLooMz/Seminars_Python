# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

a = []
for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            a.append(not (x or y or z))
            print('NOT(',x,'OR',y,'OR',z,') =',not (x or y or z))

b = []
for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            b.append(not x and not y and not z) 
            print('NOT',x,'AND NOT',y,'AND NOT',z,'=',not x and not y and not z)           

for i in range(8):
    if a[i] == b[i]:
        print(f'{a[i]} = {b[i]}: Утверждение истинно')
    else:
        print('Утверждение ложно')