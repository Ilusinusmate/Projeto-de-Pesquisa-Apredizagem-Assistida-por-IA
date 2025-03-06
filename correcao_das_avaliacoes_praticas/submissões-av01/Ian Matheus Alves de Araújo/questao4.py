n = int(input())
m = int(input())
p = 0
if n >= 0 and n <= m:
    for i in range (n,m+1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            continue
        else:
            p += 1
            print(i)
if p == 0:
    print('Nenhum número primo encontrado')
