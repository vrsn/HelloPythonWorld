for i in range(1, 3):
    print("Current value is {}".format(i))
print("*" * 80)
print("Variable 'i' ({}), used for the iteration, still exists and can be accessed!!!".format(i))


name = "Vova"
age = int(input("How old are you, {}? ".format(name))) # crashes if stringis received

if age < 18:
    print("You have to wait {} years to vote, sorry...".format(18 - age))
elif age >100:
    print("Sorry, you are too old to vote")
else:
    print("Old enough to vote, but not too old!")

print("*" * 80)

if age>=18 and age<100:
    print("Vote")
else:
    print("Don't vote")

if 18 <= age < 100:
    print("Vote")

if "string":
    print("Truthy!")
