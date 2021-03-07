low = 1
high = 1000

print("Think of a number between {} and {}.".format(low, high))
print("When you are ready, press ENTER.")
key_pressed = input()

print("Please answer with\n"
      "'c' if I guessed correctly\n"
      "'l' if I should guess lower\n"
      "'h' if I should guess higher.")

low = low-1
guess = 1
guesses = 1
while low < high:

    print("\tGuessing in range of {} to {}".format(low, high))

    mid = ((high - low) // 2)
    if mid == 0:
        mid = 1

    guess = low + mid
    print("Your number is {}?".format(guess))
    user_input = input()

    if user_input == 'c':
        print("That was easy :-). I needed only {} tries to get there!".format(guesses))
        break
    elif user_input == 'h':
        low = guess
    elif user_input == 'l':
        high = guess
    else:
        print("Please see the instruction and use correct input.")

    guesses += 1