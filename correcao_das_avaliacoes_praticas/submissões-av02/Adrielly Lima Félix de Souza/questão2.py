lista = []

for i in lista:
    soma = i + 1
    print(soma)


media_aritmetica = ( soma / len(lista))
print(media_aritmetica)


if len(lista) % 2 == 1:
    meio = len(lista) // 2
    print(lista[meio])


else:
    direita = len(lista) // 2
    esquerda = len((lista) / 2) - 1
    print((lista[direita] + lista[esquerda]) / 2)