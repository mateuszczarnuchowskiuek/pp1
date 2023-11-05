#17. Define the function different(n1,n2,n3), which returns True if all three numbers n1,n2,n3 are different or False otherwise. Then, write a program that reads three integers from the keyboard. Checks whether the numbers are different. Sample result:
#Enter first number: …
#Enter second number: …
#Enter third number: …
#Numbers …, …, and … are different

def different(n1,n2,n3):
    if n1 != n2 and n2 != n3 and n1 != n3:
        return True
    else:
        return False

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

if different(num1,num2,num3):
    print(f'Numbers {num1}, {num2}, {num3} are different')