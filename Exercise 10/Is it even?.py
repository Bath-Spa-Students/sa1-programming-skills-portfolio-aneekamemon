# Is it even?

'''

Write a program that tests if a value is even or odd. Follow the instructions
outlined below:

Instructions:
• The program should ask the user for a number from within the main
function.

• The entered number should be passed to a function that determines if the
value is even or odd.

• The function should return a message indicating whether the number is
even or odd.

• The message returned by the function should be printed from within the
main function.

# This has been copied from the exercise sheet.

'''

# The main function where we can observe if a integer is odd or even.

def odd_or_even(num):
    if num % 2 == 0: # If the integer can be divided into 2, then it is even...
        return (f"{num} is an even number.")
    else:
        return (f"{num} is an odd number.") # If the integer can't be divided into 2, then it is odd...
    
def main(): # This main function is responsible for user input
        user_input = int(input("Enter a number: ")) # user is asked to enter a number
        final_result = odd_or_even(user_input)  # The odd_or_even function gets called to determine whether the number entered is odd or even...
        print (final_result)    # This will print the result
if __name__ == "__main__":
    main()      # If run directly, this will only run the 'main' function.

