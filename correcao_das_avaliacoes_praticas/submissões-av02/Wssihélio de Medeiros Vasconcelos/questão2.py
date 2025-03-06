l = list(map(float, input().split()))
print(sum(l))
print(sum(l)/len(l))
l = sorted(l)
if len(l) % 2 == 0:
    print((l[int((len(l)/2))-1] + l[int((len(l)/2))])/2)
else:
    print(l[int(len(l)/2)])