a = int(input())
b = int(input())
c = int(input())
delta = b**2 - 4*a*c
if delta<0:
    print('Delta negativo')
elif delta==0:
    print('Raiz única:', (-b)/(2*a))
else:
    print('Raízes:', ((-b)+delta**(1/2))/(2*a), 'e', ((-b)-delta**(1/2))/(2*a))