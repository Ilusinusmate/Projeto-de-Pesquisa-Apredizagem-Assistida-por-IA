a = int(input())
b = int(input())
c = int(input())

delta = (b**2) - (4*a*c)

raiz_1 = ((-b) + (delta**0.5)) / (2*a)
raiz_2 = ((-b) - (delta**0.5)) / (2*a)

if delta > 0:
    print(f" Raízes: {raiz_1} e {raiz_2}")
    
elif delta < 0:
    print("Delta negativo")
    
if delta == 0:
    print(f"Raíz única: {raiz_1}")
