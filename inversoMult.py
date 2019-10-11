def inverso21():
    inversos = []
    for i in range(2, 21):
        if 21%i == 0:
            continue
        else:
            for j in range(2,21):
                te = (i * j) 
                if te% 21 == 1:
                    inversos.append(i)
    print(inversos)

def inverso45():
    for i in range(2, 94):
        if (i* 45)%94 == 1:
            print("inverso multiplicativo de 45 é ", i)


inverso21() 
inverso45()