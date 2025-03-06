a= float(input())
b= float(input())
c= float(input())

delta= (b**2)-4*a*c
if delta<0:
    print("Delta negativo")
    
x1= (-b+(delta**(1/2)))/2*a
x2= (-b-(delta**(1/2)))/2*a

if delta>0:
    print('Raízes:',x1,'e',x2)
    
if delta==0:
    print('Raíz única:',x1)