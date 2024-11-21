# Brute Force Attack - Optional Requirements.


'''

Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the
user enters the wrong password, inform them of the remaining attempts. If the
maximum number of attempts is reached, inform the user that the authorities
have been alerted.
# This has been copied from the exercise sheet. 

'''

# To start we must define the correct password

correct_password = "12345"                  # This code defines the correct password as 12345

num_of_attempts = 0                         #      This sets up a counter to track the amount of times a password attempt was made.

maximum_num_of_attempts = 5                 # This code sets the maximum password attempts to 10 attempts

while num_of_attempts < maximum_num_of_attempts:      # This creates a loop that continues until a correct password is entered, as it asks the user for the correct password...

    user_password = input("Enter the correct password: ") 

    num_of_attempts += 1        # This operator adds an attempt count onto the counter, after an attempt has been made; appending a attempt to the string.

    if user_password == correct_password:       # This alerts the user that the correct password has been entered, and will break the loop.
        print ("The correct password has been entered!")
        break
    else:
        attempts_remaining = (maximum_num_of_attempts - num_of_attempts)     # The minus operator will deduce the number of attempts being made from the maximum number of attempts. 


        print (f"Incorrect password, please try again!\nYou have {attempts_remaining} remaining attempts. \n")    # When incorrect, it will inform the user of the attempts remaining..

        if num_of_attempts == maximum_num_of_attempts:      # This shows that the maximum amount of attempts have been reached.
            print ("Access has been revoked, you have entered too many incorrect password attempts. AUTHORITIES HAVE BEEN ALERTED! ") # If too many attempts have been made and the password is wrong the loops ends and the user is notified. 

         
