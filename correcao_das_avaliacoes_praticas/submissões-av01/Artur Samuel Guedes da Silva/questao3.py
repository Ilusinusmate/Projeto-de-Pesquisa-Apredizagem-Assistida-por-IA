
a = float(input())
b = float(input())
c = float(input())
D = ((b**2)-(4*a*c))
r1 = ((-b)+(D**(1/2)))/(2*a)
r2 = ((-b)-(D**(1/2)))/(2*a)

if(D > 0):
    print(f'Raizes: {r1} e {r2}')
elif(D == 0):
    print(f'Raiz única: {r1}')
else:
    print(f'Delta negativo')