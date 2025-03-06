N = int(input())

if N < 0 or N > 14:
    print('fora da escala')

elif N == 7:
    print('neutro')

elif N > 7 and N <= 14:
    print('básico')

elif N >= 0 and N < 7:
    print('ácido')