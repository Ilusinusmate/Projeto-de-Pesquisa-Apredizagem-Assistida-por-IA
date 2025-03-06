a=float(input())
b=float(input())
c=float(input())
delta=b**2-4*a*c
x1= (-b + delta/4)/2*a
x2= (-b - delta/4)/2*a
if (delta <0):
    print("Delta negativo")
elif (delta > 0):
    print(" Raizes:",x1 e x2)
elif (delta==0):
    print (" raiz unica:",x1)