a = int(input())
b = int(input())
c = int(input())
delta = b^2 - 4*a*c
x1 = -b + delta**2/2*a
x2 = -b - delta**2/2*a
if delta < 0:
    print("Delta negativo")
elif delta > 0:
    print(x1 and x2)
elif delta == 0:
    print(x1)
