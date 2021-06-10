import random

bingoTick = [[]]

for b in bingoTick:
    bingoTick.append(b*9)

for y in range(15):
    for d in enumerate(bingoTick):
        bingoTick.append(random.randint(10+(y*d)))