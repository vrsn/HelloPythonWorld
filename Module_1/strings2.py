parrot = "Norwegian Blue"

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3 - 14])
print(parrot[6])
print(parrot[8 - 14])

print()

print(parrot[0:6]) # last character IS NOT INCLUDED. The same in range
print(parrot[3:5])
print()
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])

print(parrot[:])

print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[0:6:2]) # Steps in slicing

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

