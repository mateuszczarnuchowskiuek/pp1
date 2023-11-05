#Using functions and constants available in the 'math' module, write a program that calculates and displays:
#        a. natural logarithm of 5
#        b. e raised to the power of 3
#        c. square root of 7
#        d. sine of 90 degrees

import math

a = math.log(5)
b = math.exp(3)
c = math.sqrt(7)
d = math.sin(math.radians(90))

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")