lista=list(map(float,input().split()))
c=len(lista)
k=sum(lista)
print(f"{k:.1f}")
print(f"{k/c:.1f}")
lista=sorted(lista)
if c%2==0:
    print(f"{(lista[c//2-1]+lista[c//2])/2:.1f}")
else:
    print(f"{lista[c//2]:.1f}")