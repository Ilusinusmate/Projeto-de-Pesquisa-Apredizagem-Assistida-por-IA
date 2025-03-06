a=float(input())
b=float(input())
c=float(input())

delta=(b*b)-4*a*c

x1= -b+/2*a
x2= -b-/2*a

delta0=-b/2*a

if delta<0:
    print('Delta negativo')

if delta>0:
    print('Raízes: ', x1,'e', x2)

if delta==0:
    print('Raiz única:',delta0)

