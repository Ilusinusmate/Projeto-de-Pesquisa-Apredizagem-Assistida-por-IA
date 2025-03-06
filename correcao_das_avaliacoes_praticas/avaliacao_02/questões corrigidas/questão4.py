stack = []
while True:
    comando = input().lower()

    if comando[0] == "f":
        break

    elif comando[0] == "e":
        n = comando.split()[-1]
        stack.insert(0, n)
    
    elif comando[0] == "d":
        stack.pop(0)

    elif comando[0] == "i":
        
        if len(stack) == 0:
            print("[]")
            continue

        print(' '.join(stack))
