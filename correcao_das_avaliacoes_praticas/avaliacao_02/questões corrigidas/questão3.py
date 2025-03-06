hashmap = {
    "A": "G",
    "G": "A",
    "C": "T",
    "T": "C"
}

print(''.join(list(map(lambda x: hashmap[x], input()))))