l = [float(x) for x in input().split()]
print(f'{sum(l):.1f}')
print(f'{sum(l)/len(l):.1f}')
l = sorted(l)
if len(l)%2!=0 :
    print(f'{l[len(l)//2]:.1f}')
else :
    print(f'{(l[len(l)//2-1]+l[len(l)//2])/2:.1f}')