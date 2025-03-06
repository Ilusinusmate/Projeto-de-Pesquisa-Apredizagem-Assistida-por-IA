a = float(input())
b = float(input())
c = float(input())


delta = b**2 - 4*a*c

if delta < 0:
    print("Delta negativo")
elif delta == 0:
    x = -1 * (b / (2*a))
    print(f"Raiz única: {x}")
else:
    x1 = (-1*b + delta**0.5) / (2*a)
    x2 = (-1*b - delta**0.5) / (2*a)
    print(f"Raízes: {x1} e {x2}")