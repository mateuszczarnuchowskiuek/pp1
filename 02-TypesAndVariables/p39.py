price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

discounted = price - price * (discount / 100)
reduction = price - discounted

print(f"Price with discount: {discounted:.2f}")
print(f"Reduction: {reduction:.2f}")