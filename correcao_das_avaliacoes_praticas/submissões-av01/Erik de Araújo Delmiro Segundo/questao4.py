a= int(input())
b= int(input())
if a>=b:
  for i in range(b,a,1):
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
      print(i)
    else:
      print("Nenhum número primo encontrado")
elif b>a:
  for i in range(a,b,1):
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
      print(i)
    else:
      print("Nenhum número primo encontrado")
