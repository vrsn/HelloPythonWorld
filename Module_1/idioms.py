#                    1         2
#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"
#letters = ""

# reverse sequence  [::-1]
print(letters[::-1])

# last element [-1:]
print(letters[-1:])

# first element [:1]. Safe for empty strings
print(letters[:1])
print(letters[0])  # error if empty