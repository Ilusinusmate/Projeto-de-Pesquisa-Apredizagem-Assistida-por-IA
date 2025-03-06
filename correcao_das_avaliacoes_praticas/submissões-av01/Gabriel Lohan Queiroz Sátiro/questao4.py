def primo(n) :
    c = True
    if n==1 or n==0 :
        c = False
    elif n==2 :
        c = True
    else :
        for i in range (2,n//2+1) :
            if n%i==0 :
                c=False
    return c
c = 0
n,m = int(input()),int(input())
for i in range (n,m+1) :
    if primo(i) :
        print (i)
        c+=1
if c==0 :
    print ('Nenhum número primo encontrado')