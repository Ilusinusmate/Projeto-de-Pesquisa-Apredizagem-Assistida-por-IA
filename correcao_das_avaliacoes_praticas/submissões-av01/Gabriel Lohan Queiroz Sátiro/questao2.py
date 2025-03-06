target = int(input())
l = []
if target == -1 :
    print('Valor inválido')
else :
    k = int(input())
    while k!=-1 :
        l.append(k)
        k = int(input())
    print(l.count(target))