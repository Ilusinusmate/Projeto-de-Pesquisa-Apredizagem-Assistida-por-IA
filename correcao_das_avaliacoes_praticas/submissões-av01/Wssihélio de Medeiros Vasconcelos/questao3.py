a = float(input())
b = float(input())
c = float(input())

dlt = (b**2) - 4*a*c

if dlt < 0:
    print('Delta negativo')
elif dlt > 0:
    x1 = (-b + dlt**0.5)/2*a
    x2 = (-b - dlt**0.5)/2*a
    print(f'Raízes: {x1} e {x2}')
else:
    x1 = (-b + dlt**0.5)/2*a
    print(f'Raiz única: {x1}')
    