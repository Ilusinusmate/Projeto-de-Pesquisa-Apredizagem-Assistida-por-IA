n = int(input())
k = None
cont = 0
if(n == -1):
    print('Valor inválido')
    exit()
else:
    while(k != -1):
        k = int(input())
        if(k == n):
            cont += 1
print(cont)
          