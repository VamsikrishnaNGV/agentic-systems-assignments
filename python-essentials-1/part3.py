# Part 3: Age Category and Eligibility Checker
# Write a Python program that:

# Takes the user's name and age as input.
# Converts age to an integer.
# Uses conditional statements to determine the category.
# Print:

# "Hello <name>"

# Based on age:

# Age Range	Print
# Less than 13	"You are a Child"
# 13 to 17	"You are a Teenager"
# 18 to 59	"You are an Adult"
# 60 and above	"You are a Senior Citizen"
# Additionally:

# If age ≥ 18 → print "You are eligible to vote"
# Else → print "You are not eligible to vote"
# If:

# Invalid input → print "Invalid age input"
# Age is negative → print "Age cannot be negative"

name = input('Enter user name: ')

try:
    age = int(input('Enter user age: '))
    if age < 0:
        print('Age cannot be negative')
    else:
        print(f"Hello {name}")
        if age < 13:
            print('You are a Child')
        elif 13 <= age <= 17:
            print('You are a Teenager')
        elif 18 <= age <= 59:
            print('You are an Adult')
        else:
            print('You are a Senior Citizen')

        if age >= 18:
            print('You are eligible to vote')
        else:
            print('You are not eligible to vote')   
        
except ValueError:
    print('Invalid age input')        