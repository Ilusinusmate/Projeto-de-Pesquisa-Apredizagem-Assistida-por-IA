a = input().upper()
for i in range(len(a)):
    if a[i] == 'A':
        print('G', end = '')
    elif a[i] == 'G':
        print('A', end = '')
    elif a[i] == 'C':
        print('T', end = '')
    elif a[i] == 'T':
        print('C', end = '')