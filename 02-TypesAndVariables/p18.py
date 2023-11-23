x = 7
y = 34

print(f"x: {x}")
print(f"y: {y}")

#to jest normalne rozwiązanie:
#temporary = y
#y = x
#x = temporary

#ale python jest nienormalny i umożliwia takie cuda:
x , y = y , x
print(f"x after swapping: {x}")
print(f"y after swapping: {y}")