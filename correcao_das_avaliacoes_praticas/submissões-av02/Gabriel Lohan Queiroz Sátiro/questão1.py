comando = input().upper()
if comando == 'CODIFICAR' :
    s1,s2 = [x for x in input().split()]
    s3 = ''
    if len(s1)>len(s2) :
        s1 = s1[:len(s2)-1]
    elif len(s1)<len(s2) :
        s2 = s2[:len(s2)-1]
    for i in range(len(s1)) :
        s3+=s1[i]+s2[i]
    print(s3)
else :
    s = input()
    s1 = ''
    s2 = ''
    for i in range(len(s)) :
        if i%2==0:
            s2+=s[i]
        else :
            s1+=s[i]
    print(s2)
    print(s1)
        