# Biography - Exercise 3

'''
Exercise 3: Biography - 25 Marks

In this exercise, you’ll create a program that stores and prints your name, home-
town, and age to the console using a Python dictionary.

Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a
dictionary.
2. Print the values on separate lines using a single print() statement.
3. Use variables with appropriate data types for each piece of information.
# {This section has been copied from the Exercise sheet...}
'''


# Write down variables corresponding to specific personal information

# First variable is your name 
name = "Aneeka Memon"                 # Name is a string in this case

# Second variable is your hometown
hometown = "Karachi"            # hometwon is a string too

# Third variable is your age 
age = 18                # Age is a integer in this case

# Use discriptive keys to store information in a dictionary 

# use 'keys' correlated to their specific values

information = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print values in seperate lines (through the use of '\n')
# As well as using variables with appropriate data types. 


print (f"{information['name']}\n{information['hometown']}\n{information['age']}")
