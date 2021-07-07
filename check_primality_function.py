# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.

import sys

number = int(input("Please choose a number: "))
prime = False

if number > 0:
    for x in range (2, number -1):
        if number % x != 0:
            continue
        elif number % x == 0:
            sys.exit("The number is not a prime number.")
    sys.exit("The number is a prime number.")
elif number == 0:
    sys.exit("The number is not a prime number.")
else:
    sys.exit("The number is not a prime number.")

