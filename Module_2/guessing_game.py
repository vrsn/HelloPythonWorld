import random

maxvalue = 100
answer = random.randint(1, maxvalue)
guess = None
trycount = 1 # TODO: Maybe remove it.

print("Wellcome to the guess game!")
print("Please guess the number between 1 and {}, you have unlimited tries.".format(maxvalue))

while guess != answer:
    print("Try number {}: ".format(trycount))
    guess = int(input())

    if guess < answer:
        print("Слишком низко, try again:")
    elif guess > answer:
        print("Слишком высоко, try again:")
    else:
        print("Бинго!!!")

    trycount += 1

