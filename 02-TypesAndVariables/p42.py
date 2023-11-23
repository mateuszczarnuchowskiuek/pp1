number = input("Enter binary number: ")

lenght = len(number)
decimal = 0

for i in range(lenght):
    decimal += int(number[i]) * 2**(lenght-i-1)

print(f"Binary number in decimal notation: {decimal}")