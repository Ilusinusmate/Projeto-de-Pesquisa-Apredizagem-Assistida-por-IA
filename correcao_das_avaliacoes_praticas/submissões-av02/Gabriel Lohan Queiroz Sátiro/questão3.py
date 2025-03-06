dic = {
    'A' : 'G',
    'G' : 'A',
    'C' : 'T',
    'T' : 'C',   
    }
s = input().upper()
s2 = ''
for i in s :
    s2+=dic[i]
print(s2)