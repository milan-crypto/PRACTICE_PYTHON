# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.

number = int(input("Please choose a number: "))
number_two = int(input("Please choose another number: "))
mod = number % number_two

if mod != 0:
    print('You chose an odd number!')
else:
    print("You chose an even number!")
