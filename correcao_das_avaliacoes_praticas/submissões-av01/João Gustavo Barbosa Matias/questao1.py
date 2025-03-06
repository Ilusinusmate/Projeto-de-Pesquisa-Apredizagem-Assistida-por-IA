n=int(input())
if n<0 or n>14:
    print("fora da escala")
elif n==7:
    print("neutro")
elif n<7:
    print("ácido")
else:
    print("básico")