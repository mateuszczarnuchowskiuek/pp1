import random

dice = [1, 2, 3, 4, 5, 6]
roll = random.choice(dice)

guess = int(input("guess the number: "))

print(guess == roll)