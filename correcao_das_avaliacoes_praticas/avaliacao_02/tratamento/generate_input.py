import random

with open("input.txt", "w") as file:
    
    for i in range(100):
        file.write(' '.join([ str(random.randint(-1000, 1000)/(random.randint(1, 100) )) for _ in range(int(random.randint(3, 50)/2)) ]))
        file.write('\n')
        file.write('\n')
        file.write('\n')