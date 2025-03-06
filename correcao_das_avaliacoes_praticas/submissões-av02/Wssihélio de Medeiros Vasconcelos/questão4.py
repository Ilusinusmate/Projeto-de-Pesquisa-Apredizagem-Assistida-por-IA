pilha = []
while True:
    a = input().upper()
    c = a.split()
    if c[0] == 'EMPILHAR':
        pilha.append(int(c[1]))
    elif a == 'DESEMPILHAR':
        pilha.pop()
    elif a == 'FINALIZAR':
        break
    elif a == 'IMPRIMIR':
        if len(pilha) == 0:
            print(pilha)
        else:
            p1 = pilha[::-1]
            print(*p1)