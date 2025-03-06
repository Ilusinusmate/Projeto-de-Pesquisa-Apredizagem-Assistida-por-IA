n = int(input())

if  n == 7:
    print("neutro")
elif n > 7 and  n <= 14:
    print("básico")
elif n < 7 and n >= 0:
    print("ácido")
else:
    print("fora da escala")