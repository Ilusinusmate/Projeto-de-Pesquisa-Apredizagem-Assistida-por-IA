a=float(input())
b=float(input())
c=float(input())
delta=b**2+(-4*a*c)
if delta<0:
    print("Delta negativo")
elif delta==0:
    raiz=(b*(-1))/(2*a)
    print("Raiz única:",raiz)
else:
    delta=delta**(1/2)
    raiz1=((b*(-1))+delta)/(2*a)
    raiz2=((b*(-1))-delta)/(2*a)
    print("Raízes:",raiz1,"e",raiz2)