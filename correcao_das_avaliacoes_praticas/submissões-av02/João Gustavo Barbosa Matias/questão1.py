comando=input().upper()
if comando=="CODIFICAR":
    n,n2=input().split()
    for i in range(min(len(n),len(n2))):
        print(n[i]+n2[i],end="")
else:
    n3=input()
    n,n2="",""
    for i in range(len(n3)):
        if i%2==0:
            n+=n3[i]
        else:
            n2+=n3[i]
    if len(n)>len(n2):
        n=n[:len(n2):]
    print(n,"\n"+n2)