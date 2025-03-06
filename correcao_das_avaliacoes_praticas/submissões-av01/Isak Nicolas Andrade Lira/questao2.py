n=int(input())
cont=0
if n==-1:
    print('Valor inválido')
    
else:
    while True:
     k=int(input())
     if k==n:
         cont+=1
     elif k==-1:
        break
    print(cont)
