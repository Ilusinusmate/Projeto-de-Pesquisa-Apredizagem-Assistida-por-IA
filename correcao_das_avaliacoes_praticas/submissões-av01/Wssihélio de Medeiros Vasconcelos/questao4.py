c = 0
for i in range(int(input()), int(input()) + 1):
    if i == 2 or i == 3 or  i == 5 or i == 7 or i == 11 or i == 13:
        print(i)
        c += 1
    elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0 and i % 13 != 0:
        print(i)
        c += 1
if c == 0:
    print('Nenhum número primo encontrado')