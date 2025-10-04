heads = 35
legs = 94
for chickens in range(heads + 1):
    rabbits=heads-chickens  
    if 2 *chickens+4*rabbits==legs:
        print("Chickens:", chickens)
        print("Rabbits:", rabbits)