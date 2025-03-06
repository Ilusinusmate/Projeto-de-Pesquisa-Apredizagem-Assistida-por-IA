pilha = []
comando= input()

while True:
    if comando == "Empilhar":
        item = int(input())
        pilha.insert(0, item)
    if comando == "Desempilhar":
        pilha.pop
    if comando == "Imprimir":
        print(*pilha)
    if comando == "Finalizar":
        break
 