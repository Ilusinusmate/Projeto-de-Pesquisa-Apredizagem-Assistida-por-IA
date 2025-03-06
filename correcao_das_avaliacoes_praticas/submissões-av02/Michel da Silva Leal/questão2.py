lista=[]
a=0
while True:
    a=int(input())
    lista.append(a)
    if a == -1:
        break
    b = sum(lista)
    c = b/len(lista)
print(b)
print(c)

    
    