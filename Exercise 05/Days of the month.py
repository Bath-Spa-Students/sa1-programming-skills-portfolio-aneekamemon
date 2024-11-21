
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

days_of_the_month = {

# num of days in the months  # MONTHS
1: 31,                  # January
2: 28,                  # February
3: 31,                  # March
4: 30,                  # April
5: 31,                  # May
6: 30,                  # June
7: 31,                  # July
8: 31,                  # August
9: 30,                  # September
10: 31,                 # October
11: 30,                 # November
12: 31,                 # December

}


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
try: 
    month_num = int(input("Please enter a number between 1 to 12 in accordance to the months: ").strip())
    if month_num in (days_of_the_month):    # Checks the validity of the number entered (whether or not it is in the dictionary...)
        suffix = ordinal_suffix(month_num)      # Places suffix after month number
        print (f"The number of days in the {month_num}{suffix} month is {days_of_the_month[month_num]}.")
    else:       # Redirects user to only enter numbers between 1 to 12.
        print ("That isn't a valid month number. Please try to enter a number between 1 to 12. ")
except ValueError:      # Asks to enter integers between 1-12 only...
    print ("Invalid input... Please enter a numerical number between the range of 1 to 12.")
