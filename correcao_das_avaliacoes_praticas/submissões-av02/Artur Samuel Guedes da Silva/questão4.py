pile = []
ent = ''
while True:
    ent = input()
    if (ent[0] == 'E'):
        ent = ent.split(' ')
        pile.append(int(ent[-1]))
    elif(ent[0] == 'F'):
        break
    elif(ent[0] == 'I'):
        print(sorted(pile).reverse(), end == ' ')
    elif(ent[0] == 'D'):
        pile == pile.remove()
    
    
        
        