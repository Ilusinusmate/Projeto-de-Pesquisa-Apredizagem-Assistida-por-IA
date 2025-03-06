pH= int(input())
if pH<0 or pH>14:
    print('fora da escala')

elif pH==7:
    print('neutro')
    
elif pH>7 and pH<=14:
    print('básico')
    
elif pH>=0 and pH<7:
    print('ácido')