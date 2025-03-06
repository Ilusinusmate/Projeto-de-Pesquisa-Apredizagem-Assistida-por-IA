base = input()
nbase = ''
for i in(base):
    if (i == 'A'):
        nbase += 'G'
    elif (i == 'G'):
        nbase += 'A'
    elif (i == 'C'):
        nbase += 'T'
    elif (i == 'T'):
        nbase += 'C'
print(nbase)