# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

string = str(input("Please choose a string: "))
reverse = string[::-1]
print(reverse)

if string == reverse:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome!")
