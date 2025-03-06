l = list(map(float, input().split()))
print(sum(l))
print(sum(l)/len(l))


l.sort()

if len(l) % 2 == 0:
    print((l[len(l)//2 - 1] + l[len(l)//2]) /2)
else:
    print(l[len(l)//2])