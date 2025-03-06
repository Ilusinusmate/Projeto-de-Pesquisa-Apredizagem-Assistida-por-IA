n=int(input())
if n==-1:
    print("Valor inválido")
else:
    k=int(input())
    i=0
    while k!=-1:
        if k==n:
            i+=1
        k=int(input())
    print(i)