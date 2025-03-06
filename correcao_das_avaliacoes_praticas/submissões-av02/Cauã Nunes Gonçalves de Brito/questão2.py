a=int(input())
lista=[]
for i in range(a):
    lista.append(float(input()))
print(sum(lista))
print(sum(lista)/len(lista))
if a%2==1:
    meio=sum(lista)/len(lista)
    print(meio)
if a%2==0:
    meio=sum(lista)/(lista[-1])
    print(meio)