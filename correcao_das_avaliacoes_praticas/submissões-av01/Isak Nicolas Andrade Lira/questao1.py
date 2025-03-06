ph=int(input())
if ph<0 or ph>14:
    print('fora da escala')
elif ph==7:
    print('neutro')
elif ph>7 and ph<=14:
    print('básico')
elif ph>=0 and ph<7:
    print('ácido')