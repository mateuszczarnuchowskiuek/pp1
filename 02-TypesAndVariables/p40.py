number = input("Enter credit card number: ")

parsed = ""

for i in range(len(number)//4):
    parsed += number[i*4]
    parsed += number[i*4+1]
    parsed += number[i*4+2]
    parsed += number[i*4+3]
    parsed += " "

print(parsed)