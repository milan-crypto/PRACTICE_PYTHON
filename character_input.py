# Create a program that asks the user to enter their name and age. Print out a message addressed to them that tells
# them the year that they will turn 100 years out.
# EXTRAS: Add on to the previous program by asking the user for another number and printing out that many copies of the
# previous message.
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as
# pressing the ENTER button)

name = input("What is your name: ")
age = int(input("What is your age: "))
current_year = int(input("What year is it? "))
year = str((current_year - age) + 100)
print(name + " will be 100 in the year " + year)
