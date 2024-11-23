# Dictionaries:

'''
Use a dictionary to store information about a person you know.Store their first name,
last name, age, and the city in which they live.
You should have keys such as first_name, age, and city. Print each piece of information stored in your dictionary.

# This has been taken from the bonus exercise sheet.
'''
# Write down the information about the person you know, corresponding to specific variables.

# First variable is their first name
first_name = "Ali"                 # first_name is a string in this case

# Second variable is your hometown
last_name = "Memon"           # last_name is a string too

# Third variable is the age 
age = 15             # Age is a integer in this case

# City they live in...
city_name = "Karachi"

# Use discriptive keys to store information in a dictionary 

# use 'keys' correlated to their specific values

information_dictionary = { 'fname': first_name, 'lname': last_name, 'age': age, 'name of their city': city_name}    # Use a dictionary with keys and items to store their information

# Print values in seperate lines (through the use of '\n')

# As well as using variables with appropriate data types. 

print (f"\n{information_dictionary['fname']} \n\n{information_dictionary['lname']} \n\n{information_dictionary['age']} \n\n{information_dictionary['name of their city']}\n")
# This print code will print out all the information about your person, in seperate lines.
