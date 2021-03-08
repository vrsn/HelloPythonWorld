option1 = "Option 1"
option2 = "Option 2"
option3 = "Option 3"
option4 = "Option 4"
option5 = "Option 5"
option6 = "Option 6"
option7 = "Option 7"
option8 = "Option 8"
exit_option = "Exit"

options = [option1, option2, option3, option4, option5, option6, option7, option8]


def print_options(options_to_print):
    for i in range(len(options_to_print)):
        print("{}. {}".format(i+1, options_to_print[i]))
    print("{}. {}".format(0, exit_option))


print("Please select an option from the list:")
print_options(options)

exit_is_chosen = False

while not exit_is_chosen:
    user_input = input()
    if user_input.isdigit():
        index = int(user_input)
        if index == 0:
            print("Possibly, the best option... Bye!")
            exit_is_chosen = True
        elif index <= len(options):
            print("You choose '{}. {}' - what a great option!".format(index, options[index-1]))
        else:
            print("Please enter a number to chose an option.")
    else:
        print("Please enter a number to chose an option.")