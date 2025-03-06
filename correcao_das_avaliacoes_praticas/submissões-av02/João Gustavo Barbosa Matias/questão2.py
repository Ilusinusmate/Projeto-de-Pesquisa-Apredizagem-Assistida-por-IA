l=[float(n) for n in input().split()]
l.sort()
suma=(sum(l))
media=sum(l)/len(l)
if len(l)%2==0:
    mediana=(l[len(l)//2]+l[len(l)//2-1])/2
else:
    mediana=(l[len(l)//2])
print(suma)
print(media)
print(mediana)