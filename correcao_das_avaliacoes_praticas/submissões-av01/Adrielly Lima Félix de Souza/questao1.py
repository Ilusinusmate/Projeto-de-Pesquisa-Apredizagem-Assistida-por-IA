ph = int(input())
if 0 < ph > 14:
    print("fora da escala")
elif ph == 7:
    print("neutro")
elif 7 < ph <= 14:
    print("básico")
elif 0 <= ph < 7:
    print("ácido")