n= int(input())
m= int(input())
divisor= 0
cont= 0
for i in range (n,m):
    divisor+=1
    a= n%divisor
    if a==0:
        cont+=1
        if cont>=2 and n!=divisor:
            cont= cont-1
    
