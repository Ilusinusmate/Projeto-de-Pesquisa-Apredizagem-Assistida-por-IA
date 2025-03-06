a= int(input())
b= int(input())
c= int(input())
d= b**2-4*a*c
x1= (-b+d**0.5)/(2*a)
x2= (-b-d**0.5)/(2*a)
if d < 0:
  print("Delta negativo")
elif d == 0:
  print(f"Raiz única:{x1}")
elif d > 0:
  print(f"Duas raízes reais: {x1} e {x2}")
print(d)
