# Advanced Requirements of Exercise 03

'''
Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the
values. Try giving both your first and second name when asked for your name.
What happens? How can you handle multiple words in Python? Test the
program by entering a string value for age (e.g., “twenty”). What happens?
How can you prevent this issue?
# This has been copied from the Exercise sheet...
'''

# Extract input from the user; such as their full name, hometown, and age.

# Both name and hometown must be entered as string data types...

user_name = input ("Please enter your full name: ")
user_hometown = input ("Please enter your hometown: ")

# To ensure that integers will be processed as the age (eg. 20, instead of Twenty). A loop must be used...

while True:    
    try:
        user_age = int(input("Please enter your age: "))
        break
    except ValueError:
        print ("Please enter your numerical age instead...")



# title
print ("\nYour Input... " "\n\n")


# this will print {full name}
print (f"Full name: {user_name}" "\n\n")

# this will print {hometown}

print (f"Hometown: {user_hometown}" "\n\n")

# this will print {age}

print (f"Age: {user_age}" "\n\n")
