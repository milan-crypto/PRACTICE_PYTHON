# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
import math

# Taking Inputs
lower = int(input("Enter Lower number:- "))

# Taking Inputs
upper = int(input("Enter Upper number:- "))

# generating random number between the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " tries")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")

# Better to use This source Code on pycharm!


# import random
#
#
# MINIMUM = 1
# MAXIMUM = 9
# NUMBER = random.randint(MINIMUM, MAXIMUM)
# GUESS = None
# ANOTHER = None
# TRY = 0
# RUNNING = True
#
# print "Alright..."
#
# while RUNNING:
#     GUESS = raw_input("What is your lucky number? ")
#     if int(GUESS) < NUMBER:
#         print "Wrong, too low."
#     elif int(GUESS) > NUMBER:
#         print "Wrong, too high."
#     elif GUESS.lower() == "exit":
#         print "Better luck next time."
#     elif int(GUESS) == NUMBER:
#         print "Yes, that's the one, %s." % str(NUMBER)
#         if TRY < 2:
#             print "Impressive, only %s tries." % str(TRY)
#         elif TRY > 2 and TRY < 10:
#             print "Pretty good, %s tries." % str(TRY)
#         else:
#             print "Bad, %s tries." % str(TRY)
#         RUNNING = False
#     TRY += 1
