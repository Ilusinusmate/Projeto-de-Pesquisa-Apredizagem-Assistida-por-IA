ph=int(input())
if ph<0 or ph>14:
    print('fora da escala')
if ph==7:
    print('neutro')
if ph>7 and ph<=14:
    print('básico')
if ph>=0 and ph<7:
    print('ácido')