a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4*a*c

if delta < 0:
    print('Delta negativo')
if delta == 0:
    print('Raiz única: ', -b/2*a)
if delta > 0:
    print('Raízes: ', -b+ (delta**1/2)/2*a, 'e', -b - (delta**1/2)/2*a)
