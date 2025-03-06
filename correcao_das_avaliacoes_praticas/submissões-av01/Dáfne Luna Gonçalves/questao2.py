a=0
cont= 0
numero= int(input())
while a==0:
    if numero==-1:
        print('Valor inválido')
        break
        
    k= int(input())
    if k==-1:
        a= -1
    elif k==numero:
        cont+=1
if cont!=0:    
    print(cont)        
