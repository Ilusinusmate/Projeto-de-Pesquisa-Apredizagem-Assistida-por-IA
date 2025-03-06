n = int(input())

if 0 <= n < 7:
  print("ácido")

elif n == 7:
  print("neutro")

elif 7 < n <= 14:
  print("básico")

elif 0 > n or n > 14:
  print("fora da escala")
