a=input()
s1=""
s2=""
s3=""
if a=="CODIFICAR":
    s1,s2=input().split()
    c=len(s1)
    u=len(s2)
    if c<u:
        for x in range(c):
            s3+=s1[x]+s2[x]
    else:
        for x in range(u):
            s3+=s1[x]+s2[x]
    print(s3)
else:
    a=input()
    for x in range(len(a)):
        if x%2==0:
            s1+=a[x]
        else:
            s2+=a[x]
    print(s1)
    print(s2)