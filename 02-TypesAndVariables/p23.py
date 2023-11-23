a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))

p = (a+b+c)/2
area = (p*(p-a)*(p-b)*(p-c))**0.5
circumference = a+b+c

print(f"triangle area: {area}")
print(f"triangle circumference: {circumference}")