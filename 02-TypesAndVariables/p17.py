a = 5 + 5 * 10
print(a)

b = 3 - 2 + 1
print(b)

c = 2 + -3
print(c)

d = 2 ** 8
print(d)

e = 4 + 4 / 2 ** 2
print(e)

f = 4 % 3 % 2 % 1
print(f)

g = 1 + 2 % 3 ** 4 * 5
print(g)

h = True != False
print(h)

i = 2 <= 3 or False
print(i)

j = not True or not False and not True
print(j)

k = 2<3 and 4<5 or not 6<7
#  true     true       true
#   true and true or false
#     true or false
#         true
print(k)

l = 2 % 3 < 4 / 5 and 6 + 7 < 8 or not 9 + 10 == 19
#     2  <  0.8   and   13 < 8  or not 19 == 19
#        false   and    false   or  not  true
#         false  and    false   or  false
#               false     or      false
#                        false
print(l)

# wow, że w pythonie się tak da 😯
m = 0x11 + 0b11 + 11
print(m)