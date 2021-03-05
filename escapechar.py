splitString = "This \tstring \thas \tbeen \nsplit over\nseveral\nlines"
print(splitString)

print('The pet shop owner said "No, no, \'e\'s wtf we are writing"')

print("""The pet "That 'shit' we wrote" """)

newSplitWayString = """This string
has been
split \
but not this \
time"""

print(newSplitWayString)

num = "Number"
outString = num + " 1 \t TheLarch\n" + num + " 2 \t The Horse Chestnut"
print(outString)

print("C:\\Users\\titty\\nice...") # This is preferable
print(r"C:\Users\titty\nice...")  # raw string does not work with escape chars.

stringVar = "some string"
intVar = 455

print(type(stringVar))
print(type(intVar))

age = 2
print(age)

age = "2 days"  # Rebound the label "age" to the string instead of integer. REBOUND - not reassigned the variable.
print(age)

age = 2
age_in_words = "5 years"
print(num + " is" + age + " an error") # TypeError: can only concatenate str (not "int") to str


