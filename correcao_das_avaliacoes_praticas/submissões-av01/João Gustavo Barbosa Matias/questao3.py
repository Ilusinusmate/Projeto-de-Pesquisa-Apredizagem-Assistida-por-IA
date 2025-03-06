a,b,c=float(input()),float(input()),float(input())
d=(b**2)-(4*a*c)
if d>0:
    print(f"Raizes: {(-b+d**(1/2))/(2*a)} e {(-b-d**(1/2))/(2*a)}")
elif d==0:
    print(f"Raiz única: {(-b+d**(1/2))/(2*a)}")
else:
    print("Delta negativo")