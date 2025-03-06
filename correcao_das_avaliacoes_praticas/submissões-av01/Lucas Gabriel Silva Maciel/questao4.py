m=int(input())
n=int(input())
c=0
for x in range(m,n+1):
    a=True
    if x==0 or x==1:
        continue
    for i in range(2,x//2+1):
        if x%i==0:
            a=False
            break
    if a:
        print(x)
        c+=1
if c==0:
    print("Nenhum número primo encontrado")