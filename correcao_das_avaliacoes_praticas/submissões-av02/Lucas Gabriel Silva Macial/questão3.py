a=input()
u=""
for x in a:
    if x=="A":
        u+="G"
    elif x=="G":
        u+="A"
    elif x=="C":
        u+="T"
    else:
        u+="C"
print(u)