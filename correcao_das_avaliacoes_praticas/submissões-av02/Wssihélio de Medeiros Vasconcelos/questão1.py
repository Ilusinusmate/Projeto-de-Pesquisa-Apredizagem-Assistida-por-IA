douc = input().upper()
if douc =='CODIFICAR':
    a1, a2 = input().split()
    for i in range(len(a1)):
        print(a1[i], end = '')
        print(a2[i], end = '')
else:
    c = 0
    c1 = 0
    p = ''
    im = ''
    b1 = input()
    for i in range(len(b1)):
        if i % 2 == 0:
            p += b1[i]
        else:
            im += b1[i]
    print(p)
    print(im)