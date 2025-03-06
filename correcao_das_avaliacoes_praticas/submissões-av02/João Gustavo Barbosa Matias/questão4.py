pilha=[]
comando=input().lower().split()
while comando[0]!="finalizar":
    if comando[0]=="empilhar":
        pilha.append(comando[1])
    elif comando[0]=="desempilhar" and len(pilha)!=0:
        pilha.pop()
    elif comando[0]=="imprimir":
        if len(pilha)!=0:
            l=pilha.copy()
            l.reverse()
            l=" ".join(l)
            print(l)
        else:
            print("[]")
    comando=input().lower().split()
