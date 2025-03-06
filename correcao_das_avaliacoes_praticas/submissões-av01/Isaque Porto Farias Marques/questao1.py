pH = int(input())

if pH < 0:
    print("fora da escala")
    
if pH == 7:
    print("neutro")
    
if pH >=0 and pH < 7:
    print("ácido")
    
if pH > 14:
    print("fora da escala")
    
if pH > 7 and pH <= 14:
    print("básico")
    


    