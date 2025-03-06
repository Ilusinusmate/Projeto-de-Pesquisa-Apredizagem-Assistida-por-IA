# - sessão de variáveis
n = int(input())

# - sessão de processamento
if((n < 0) or (n > 14)):
    print('fora da escala')
elif(n == 7):
    print('neutro')
elif((n > 7) and (n <= 14)):
    print('básico')
elif((n >= 0) and (n < 7)):
    print('ácido')