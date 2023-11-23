number = input("enter vehicle registration number: ")

if(number[:2] == "KR" or number[:2] == "KK"):
    print(f"Car from Kraków: {True}")
else:
    print(f"Car from Kraków: {False}")