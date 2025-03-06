n = int(input())
m = int(input())
c = True
if n <= 2:
    if m>=2:
        print(2)
        c = False
    n=3
elif n%2==0:
    n+=1
for i in range(n, m+1, 2):
    if i!=1:
        primo = True
        for j in range(2, i):
            if i%j == 0:
                primo = False
                break
        if primo:
            print(i)
            c = False
if c or n==0 and m==0:
    print('Nenhum número primo encontrado')