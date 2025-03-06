import pathlib
import os

dir = pathlib.Path(__file__).parent
def treat(l: list[str]):
    res = ""
    l = list(map(float, l.split()))
    res += str(sum(l)) + "\n"
    res += str(sum(l)/len(l)) + "\n"


    l.sort()

    if len(l) % 2 == 0:
        res += str((l[len(l)//2 - 1] + l[len(l)//2]) /2)+ "\n"
    else:
        res += str(l[len(l)//2]) + "\n"

    return res


with open(dir / "subtarefa1.txt", "r") as file:
    data = file.read().split("\n")
        

with open(dir / 'ouput.txt', "w") as file:
    for i in data:
        file.write(treat(i))
        file.write("\n")
        file.write("\n")
    
    