a,b,c = float(input()),float(input()),float(input())
delta = b**2-4*a*c
if delta<0 :
    print ('Delta negativo')
elif delta==0 :
    print (f'Raiz única: {-b/2*a:.1f}')
else :
    raiz1 = ((-b+delta**(1/2))/2*a)
    raiz2 = ((-b-delta**(1/2))/2*a)
    print (f'Raízes: {raiz1:.1f} e {raiz2:.1f}')