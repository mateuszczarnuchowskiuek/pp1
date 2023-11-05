#12. Write a program that checks that two people are adults. Read people’s data from the keyboard. Sample result:
#Enter first person name: Peter
#Enter first person age: 21
#Enter second person name: Ann
#Enter second person age: 18
#Both Peter and Ann are adults

person1name = str(input('Enter first person name: '))
person1age = int(input('Enter first person age: '))
person2name = str(input('Enter first person name: '))
person2age = int(input('Enter first person age: '))

if person1age >= 18 and person2age >= 18:
    print(f'both {person1name} and {person2name} are adults')