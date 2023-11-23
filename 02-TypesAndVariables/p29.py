import random

dice = [1, 2, 3, 4, 5, 6]
sum = 0

for i in range(3):
    roll = random.choice(dice)
    print(f"rolled: {roll}")
    sum += roll

print(f"sum: {sum}")