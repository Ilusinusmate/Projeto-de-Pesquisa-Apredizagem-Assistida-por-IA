lista = list(map(float,input().split()))

media_aritimetica = sum(lista)/len(lista)

soma = sum(lista)


print(float(soma))
print(media_aritimetica)
quantidade_de_numeros_na_lista = len(lista)

if quantidade_de_numeros_na_lista % 2 == 0:
    meio = quantidade_de_numeros_na_lista  
    mediana = lista[meio] + lista[meio - 1]//2
    print(float(mediana))
else:
    indice = (quantidade_de_numeros_na_lista - 1)//2
    mediana = lista[indice]
    print(float(mediana))