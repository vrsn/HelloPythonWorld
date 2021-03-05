age = 24
print("What a nice number " + str(age))
print("What a {0} nice number {0}".format(age))

for i in range(5,13):
    print("No. {0:2} squared is {1:4} and cubed is {2:5}".format(i,i**2,i**3))

print()

for i in range(5,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i,i**2,i**3))

print()

for i in range(5,13):
    print("No. {} squared is {} and cubed is {:5}".format(i,i**2,i**3))

print("Pi is {0:12}".format(22/7))
print("Pi is {0:12f}".format(22/7))
print("Pi is {0:52.50f}".format(22/7))
print("Pi is {0:<72.50f}".format(22/7))
print("Pi is {0:<72.60f}".format(22/7))

# f-string
print(f"Some number {age} and it's an f-string")
print(f"Pi is {22/7:<72.50f}")
pi = 22/7
print(f"Pi is {pi:<72.50f}")

# note that string interpolation is DEPRECATED and is not to be used if Python 3.
print("This time the number is %d" % age)
print("This time the number is %f" % (22/7))
print("This time the %s is %d" % ("number", age))

