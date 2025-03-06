a=input()
lista=[]
while a!="Finalizar":
    if a=="Desempilhar":
        lista.pop()
    elif a=="Imprimir":
        if len(lista)>0:
            print(*reversed(lista))
        else:
            print("[]")
    else:
        c,g=a.split()
        g=int(g)
        lista.append(g)
    a=input()