# Days of the Month - Advanced Requirement:

'''

Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For
February, ask the user if the year is a leap year and adjust the number of days
accordingly.
# This has been copied from the exercise sheet.
'''


# Days of the Month (Exercise 05)

'''
Instructions:

1. Create a Dictionary: Define a dictionary where the keys are month num-
bers and the values are the number of days in those months.

2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid
and print the number of days in the corresponding month.
# This has been copied from the exercise sheet...
'''


# Create a dictionary and use it to store the number of days in each month. 

# Use 1 - 12 keys to represent the number of months...
# The values in the keys will be the days in each given month

# Dictionary of the days in each given month:
# num of days in the months  # MONTHS

days_of_the_month = {1: 31,2: 28,3: 31,4: 30,5: 31,6: 30,7: 31,8: 31,9: 30,10: 31,11: 30,12: 31,}


# This code ensures that there is a suffix placed after the a month number is added...

def ordinal_suffix(number):
    if 12 <= (number):     #if a number is 12 or below, then the suffix will be "th"
        return "th"
    last_digit = (number)
    if last_digit == 1: #if the number 1 is entered, then the suffix will be "st"
        return "st"
    elif last_digit == 2: #if the number 2 is entered, then the suffix will be "nd"
        return "nd"
    elif last_digit == 3: #if the number 3 is entered, then the suffix will be "rd"
        return "rd"
    else: 
        return "th" #otherwise the suffix will be "th"
    
# Ask the user for an input on the month number

# .strip() ensures removal of unnecessary whitespace

# Ensure the month number is in the valid range

while True:


    month_num = int(input("Please enter a number between 1 to 12 in accordance to the months: "))
    
    
    if month_num in (days_of_the_month):    # Checks the validity of the number entered (whether or not it is in the dictionary...)
        suffix = ordinal_suffix(month_num)      # Places suffix after month number
        
        # This is for the leap year section of the exercise 
        # In the case that a leap year occurs in the second month (February), the user needs to be questioned whether or not the year is a leap year.
        
        
        if month_num == 2:
            if_leap_year = input ("Is this particular February a leap year? (yes or no): ").lower().strip()     # '.lower' changes all text to lowercase
            days = 29 if if_leap_year == "yes"   else 28       # If the user types in "yes, then the amount of days that will show at the terminal is 29, otherwise it will be 28.
        else: 
            days = days_of_the_month[month_num]
        
        
        
        print (f"The number of days in the {month_num}{suffix} month is {days}. ")
    else:      # Redirects user to only enter numbers between 1 to 12.
        print ("That isn't a valid month number. Please try to enter a number between 1 to 12. ")
