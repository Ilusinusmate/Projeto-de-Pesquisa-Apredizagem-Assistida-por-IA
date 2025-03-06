pH= int(input())
if 0<=pH<7:
  print("ácido")
elif pH==7:
  print("neutro")
elif 14>=pH>7:
  print("básico")
elif pH<0 or pH>14:
  print("fora da escala")
