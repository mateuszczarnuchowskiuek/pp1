import random

dice = [1, 2, 3, 4, 5, 6]
roll = random.choice(dice)

print(f"Dice rolled: {roll}")
print(f"Special number: {roll == 1 or roll == 6}")