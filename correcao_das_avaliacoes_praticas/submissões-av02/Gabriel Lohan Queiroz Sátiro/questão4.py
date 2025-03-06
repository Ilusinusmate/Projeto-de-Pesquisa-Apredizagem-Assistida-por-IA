d = [x for x in input().split()]
dec = d[0]
pilha = []
l = []
while dec != 'Finalizar' :
    if dec == "Desempilhar":
        l.pop()
    elif dec == "Imprimir" :
        if len(l) == 0 :
            print('[]')
        else :
            print(*l[::-1], sep = " ")
    elif dec == "Empilhar" :
        n = int(d[1])
        l += [n]
    d = [x for x in input().split()]
    dec = d[0]