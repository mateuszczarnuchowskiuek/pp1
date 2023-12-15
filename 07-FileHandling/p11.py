file = open("numbers.txt", "r")

sum = 0

print("Numbers:", end=" ")
for line in file:
    print(int(line), end=" ")
    sum += int(line)

print(f"\nSum: {sum}")

file.close()