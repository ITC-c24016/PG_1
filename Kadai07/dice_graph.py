import random

diceNum = {i:[] for i in range(1,7)}

for i in range(1,101):
    dice = random.randint(1,6)
    diceNum[dice].append("*")

for num in range(1,7):
    print(f"{num}:{"".join(diceNum[num])}")

