n = int(input())
m = int(input())

if n <  m:
    menor = n
    maior = m
else:
    menor = m
    maior = n

primo_encontrado = False

for numero in range(menor, maior+1):
    
    if numero <= 1:
        continue

    for divisor in range(2, numero):
        if numero % divisor == 0:
            break

    else:
        primo_encontrado=True
        print(numero)  

if not primo_encontrado:
    print("Nenhum número primo encontrado")