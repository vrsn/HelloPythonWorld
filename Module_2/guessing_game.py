answer = 5

print("Please guess the name between 1 and 10: ")
guess = int(input())


if guess < answer:
    print("Too low, try again:")
    guess = int(input())
elif guess > answer:
    print("Too high, try again:")
    guess = int(input())
else:
    print("Bingo!")