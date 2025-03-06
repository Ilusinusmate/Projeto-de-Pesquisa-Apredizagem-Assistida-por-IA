n=int(input())
if n>14 or n<0:
    print("fora da escala")
elif n==7:
    print("neutro")
elif n>7:
    print("básico")
else:
    print("ácido")