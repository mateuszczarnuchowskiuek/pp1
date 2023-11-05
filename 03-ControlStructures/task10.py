#10. Write a program to calculate the absolute value of a number entered from the keyboard. Sample result:
#Enter number: -17
#|-17| = 17

number = int(input('enter number: '))

if number >= 0:
    print (f'|{number}| = {number}')
else:
    print (f'|{number}| = {-number}')
