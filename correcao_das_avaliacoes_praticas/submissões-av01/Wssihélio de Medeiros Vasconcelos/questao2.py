n = int(input())
c = 0
if n == -1:
    print('Valor inválido')
else:
    while True:
        n1 = int(input())
        if n1 == -1:
            break
        elif n1 == n:
            c += 1
    print(c)