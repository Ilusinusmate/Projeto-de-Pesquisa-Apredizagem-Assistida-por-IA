task = input()

if (task == 'CODIFICAR'):
    st = input()
    stc = []
    sign = ''
    for i in st:
        if not(i == ' '):
            stc += [i]
    '''for i in range(len(st1)+len(st2)):
        if (i%2 == 0):
            sign += st1[cont1]
            cont1 += 1
        else:
            sign += st2[cont2]
            cont2 += 1'''
elif (task == 'DECODIFICAR'):
    cod = input()
    par = ''
    im = ''
    for i in range(len(cod)):
        if i%2 == 0:
            par += cod[i]
        else:
            im += cod[i]
    print(par)
    print(im)
    