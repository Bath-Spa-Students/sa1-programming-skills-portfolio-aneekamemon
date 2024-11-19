# Brute Force Attack 
'''
Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the

3

password until they provide the correct one.
Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the
correct one is entered.
3. Output an appropriate message when the correct password is entered.
# This has been copied from the exercise sheet.
'''


# To start we must define the correct password

correct_password = "12345"           # This code defines the correct password as 12345

num_of_attempts = 0                         #      This sets up a counter to track the amount of times a password attempt was made.

maximum_num_of_attempts = 10                # This code sets the maximum password attempts to 10 attempts

while num_of_attempts < maximum_num_of_attempts:      # This creates a loop that continues until a correct password is entered, as it asks the user for the correct password...

    user_password = input("Enter the correct password: ").upper().strip()      # upper.() allows for the text to be in all caps 

    num_of_attempts += 1        # This adds an attempt count onto the counter, after an attempt has been made

    if user_password == correct_password:       # This alerts the user that the correct password has been entered, and will break the loop.
        print ("The correct password has been entered!")
        break
    else:
        print (f"Incorrect password, please try again!")    # When incorrect, it will suggest to the user to try again...

        if num_of_attempts == maximum_num_of_attempts:
            print ("Access has been revoked, you have entered too many incorrect password attempts...") # If too many attempts have been made and the password is wrong the loops ends and the user is notified. 
