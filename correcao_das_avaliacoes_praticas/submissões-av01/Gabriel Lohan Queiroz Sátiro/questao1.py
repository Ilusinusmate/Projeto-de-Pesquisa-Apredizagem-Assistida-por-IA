ph = int(input())
if ph==7 :
    print('neutro')
elif ph<7 and ph>=0:
    print('ácido')
elif ph>7 and ph<=14 :
    print('básico')
else :
    print ('fora da escala')