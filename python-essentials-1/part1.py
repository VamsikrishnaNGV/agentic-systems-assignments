# Part 1: Number Operations with Error Handling
# Write a Python program that:

# Takes two numbers as input from the user.
# Converts both inputs to integers.
# Print:

# Their sum
# Their division result
# If:

# The user enters non-numeric input → print "Invalid input"
# The second number is zero → print "Cannot divide by zero"
try:
    a = input('Enter First number: ')
    b = input('Enter Second number: ')
    
    x = int(a)
    y = int(b)

    print('Sum of two numbers: ', x+y)
    
    try:
        print('Division:',x/y)
    except ZeroDivisionError:    
        print('Cannot divide by zero')    
except ValueError:
    print('Invalid input')
