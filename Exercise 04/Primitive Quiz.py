

# Exercise 4: Primitive Quiz - 30 Marks

# INSTRUCTIONS
""" In this exercise, you’ll create a simple program that asks the user a question,
evaluates their answer, and provides feedback.

Steps:

1. Write a program that asks the user “What is the capital of France?” and
waits for their response.

2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.

3. If the answer is incorrect, the program should print a message saying the
answer is wrong """


# Ask for the input to the question ("what is the capital of France? ")

city_capital = (input("What is the capital of France? "))

# If input is correct 'paris', then print "Your answer is correct "
if city_capital == "paris": 
    print ("Your answer is correct!" )

# If input is incorrect, then print "Your answer is incorrect "

else : 
    print ("Your answer is incorrect...")