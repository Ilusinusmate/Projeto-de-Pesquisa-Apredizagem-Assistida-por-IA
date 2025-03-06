n = int(input())
if n==-1:
    print('Valor inválido')
else:
    c = 0
    k = int(input())
    while k!=-1:
        if k == n:
            c+=1
        k = int(input())
    print(c)
