n=int(input())
if n==-1:
    print("Valor inválido")
else:
    u=int(input())
    soma=0
    while u!=-1:
        if u==n:
            soma+=1
        u=int(input())
    print(soma)