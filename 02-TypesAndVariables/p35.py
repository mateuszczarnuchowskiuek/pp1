import math

circumference = float(input("Enter tree circumference: "))

diameter = circumference / math.pi

print(f"Tree can be cut down: {diameter >= 50}")