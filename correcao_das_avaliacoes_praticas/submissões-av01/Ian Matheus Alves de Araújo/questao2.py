n = int(input())
n_r = 0
while True:
    k = int(input())
    if k == n:
        n_r += 1
    if k == -1:
        break
print(n_r)
