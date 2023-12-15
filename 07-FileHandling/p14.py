file = open("shopping.txt", "a")

counter = 0
product = "none"

while product != "":
    product = input("Enter product name: ")
    if product != "":
        counter += 1
        file.write(f"{counter}. {product}\n")

file.close()