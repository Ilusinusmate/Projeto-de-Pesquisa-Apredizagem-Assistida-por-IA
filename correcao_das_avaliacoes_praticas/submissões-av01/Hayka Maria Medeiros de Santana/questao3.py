#não foi me ensinado raiz quadrada <3
a=int(input())
b=int(input())
c=int(input())
delta:(b*b)-4*a*c
if delta>0:
    x1=(-b+(d))//(2*a)
    x2=(-b-(d))//(2*a)
    if x1!=x2:
        print ("Raízes:",f"{x1:.1f}","e",f"{x2:.1f}")
    else:
        print("Raíz única:",f"{x1:.1f}")
else:
    print("Delta negativo")