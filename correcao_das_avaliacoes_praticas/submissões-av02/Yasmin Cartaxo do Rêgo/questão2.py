lista = list(map(float, input().split()))
lista.sort()
print(sum(lista))

print(sum(lista) / len(lista))


if len(lista) % 2 == 0:
    meio = int(len(lista)) // 2
    mediana = lista(meio) + lista(meio-1) / 2
    print(mediana)
else:
    meio = int(len(lista)) //2
    mediana = lista[meio]
    print(mediana)
    