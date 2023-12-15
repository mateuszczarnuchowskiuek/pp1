array = [1,2,3,4,5]
print(f"Array: {array}")

#a
array[0] -= 1
print(f"Array: {array}")

#b
array[len(array)-1] += 4
print(f"Array: {array}")

#c
array[len(array)//2] *= 2
print(f"Array: {array}")