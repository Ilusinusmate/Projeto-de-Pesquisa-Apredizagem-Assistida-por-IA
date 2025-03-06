n=int(input())
m=int(input())
condf=True
for i in range(n,m+1):
    cond=True
    if i==2:
        print(i)
        condf=False
    elif not(i==1 or i==0):
        for j in range(2,i):
            if i%j==0:
                cond=False
        if cond:
            print(i)
            condf=False
if condf:
    print("Nenhum primo encontrado")
