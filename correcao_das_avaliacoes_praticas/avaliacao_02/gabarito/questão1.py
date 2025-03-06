comando = input()

if comando == "DECODIFICAR":
    s3 = input()
    s1 = ''
    s2 = ''
    ptr = 0
    for i in range(len(s3)):
        if i % 2 == 0:
            s1 += s3[i]
        else:
            s2 += s3[i]
    print(s1)
    print(s2)

else:
    s1, s2 = input().split()
    s3 = ''
    pt1 = 0
    pt2 = 0
    for i in range(len(s1)+len(s2)):
        if i % 2 == 0:
            if pt1 >= len(s1): break
            s3 += s1[pt1]
            pt1 += 1
        
        else:
            if pt2 >= len(s2): break
            s3 += s2[pt2]
            pt2 += 1
            
    print(s3)

