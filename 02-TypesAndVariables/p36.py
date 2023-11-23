buys = float(input("enter buys: "))
sells = float(input("enter sells: "))

spread = abs(buys-sells)

print(f"Bank Buys EUR: {buys:.4f}")
print(f"Bank Sells EUR: {sells:.4f}")
print(f"Spread: {spread:.4f}")