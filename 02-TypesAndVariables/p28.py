cm = float(input("enter your height in cm: "))
kg = float(input("enter your weight in kg: "))

bmi = kg / (cm/100)**2

print(f"Your BMI index: {bmi}")
print(f"Correct weight: {18.5 <= bmi <= 24.9}")