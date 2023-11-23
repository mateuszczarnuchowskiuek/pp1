name = input("Name: ")

parsed = ""

for i in name:
    parsed += f"{i}({ord(i)}) "

print(parsed)