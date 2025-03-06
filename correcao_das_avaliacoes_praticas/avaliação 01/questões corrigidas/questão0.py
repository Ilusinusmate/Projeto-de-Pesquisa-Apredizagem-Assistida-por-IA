n = int(input())

if n == -1:
    print("Valor inválido")
    exit()

acumulador = 0
while True:
    _ = int(input())
    if _ == n:
        acumulador += 1
    elif _ == -1:
        break

print(acumulador)