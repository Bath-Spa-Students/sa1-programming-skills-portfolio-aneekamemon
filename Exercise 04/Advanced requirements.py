# Exercise 4: Primitive Quiz - 30 marks 

# INSTRUCTIONS 

""" 

Steps:

1. Write a program that asks the user “What is the capital of France?” and
waits for their response.

2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.

3. If the answer is incorrect, the program should print a message saying the
answer is wrong.


Advanced Requirements:

Ignore Capitalization: Modify your program to accept answers regardless of
the capitalization (e.g., “paris”, “Paris”, and “PaRis” should all be considered
correct). 

Multiple Questions: Extend the program into a quiz that asks for the
capitals of 10 European countries. Provide feedback for each question. """

# FIRST PORTION OF THE TASK 

# Ask for the input to the question ("what is the capital of France? ")

city_capital = (input("What is the capital of France? "))

# If input is correct 'paris', then print "Your answer is correct "

# Insert the .lower() method which ignores any uppercase letters for the answer. 
if (city_capital.lower() == ("paris")):

    print ("Your answer is correct!\n") 
    # If input is incorrect, then print "Your answer is incorrect "
else : 
    print ("Your answer is incorrect...\n")


"""Irrespective of the cases combination, 
if the answer is "paris" the answer will be correct."""



# SECOND PORTION OF THE TASK 

"""

Multiple Questions: Extend the program into a quiz that asks for the
capitals of 10 European countries. Provide feedback for each question.

"""


# 10 cities quiz

print("This is a quiz, which tests your knowledge on city capitals!\n")

# To initialize a score keeper for the correct answers

correct_answers = 0 

# Question 1 

city_capital1 = (input("1. What is the capital of Germany? \n"))

# If input is correct 'berlin', then print "Your answer is correct "

# Insert the .lower() method which ignores any uppercase letters for the answer. 
if (city_capital1.lower() == ("berlin")):

    print ("Your answer is correct!\n") 
    correct_answers += 1 

    # If input is incorrect, then print "Your answer is incorrect "
else : 
    print ("Your answer is incorrect...\n")

# Question 2

city_capital2 = (input("2. What is the capital of Greece? \n"))

# If input is correct 'athens', then print "Your answer is correct "

# Insert the .lower() method which ignores any uppercase letters for the answer. 
if (city_capital2.lower() == ("athens")):

    print ("Your answer is correct!\n") 
    correct_answers += 1 

    # If input is incorrect, then print "Your answer is incorrect "
else : 
    print ("Your answer is incorrect...\n")

# Question 3

city_capital3 = (input("3. What is the capital of Hungary? \n"))

# If input is correct 'budapest', then print "Your answer is correct "

# Insert the .lower() method which ignores any uppercase letters for the answer. 
if (city_capital3.lower() == ("budapest")):

    print ("Your answer is correct!\n") 
    correct_answers += 1 

    # If input is incorrect, then print "Your answer is incorrect "
else : 
    print ("Your answer is incorrect...\n")

# Question 4

city_capital4 = (input("4. What is the capital of Ireland? \n"))

# If input is correct 'dublin', then print "Your answer is correct "

# Insert the .lower() method which ignores any uppercase letters for the answer. 
if (city_capital4.lower() == ("dublin")):

    print ("Your answer is correct!\n") 
    correct_answers += 1 

    # If input is incorrect, then print "Your answer is incorrect "
else : 
    print ("Your answer is incorrect...\n")

# Question 5

city_capital5 = (input("5. What is the capital of Italy? \n"))

# If input is correct 'rome', then print "Your answer is correct "

# Insert the .lower() method which ignores any uppercase letters for the answer. 
if (city_capital5.lower() == ("rome")):

    print ("Your answer is correct!\n") 
    correct_answers += 1 

    # If input is incorrect, then print "Your answer is incorrect "
else : 
    print ("Your answer is incorrect...\n")

# Question 6

city_capital6 = (input("6. What is the capital of Netherlands? \n"))

# If input is correct 'amsterdam', then print "Your answer is correct "

# Insert the .lower() method which ignores any uppercase letters for the answer. 
if (city_capital6.lower() == ("amsterdam")):

    print ("Your answer is correct!\n") 
    correct_answers += 1 

    # If input is incorrect, then print "Your answer is incorrect "
else : 
    print ("Your answer is incorrect...\n")

# Question 7

city_capital7 = (input("7. What is the capital of Norway? \n"))

# If input is correct 'oslo', then print "Your answer is correct "

# Insert the .lower() method which ignores any uppercase letters for the answer. 
if (city_capital7.lower() == ("oslo")):

    print ("Your answer is correct!\n") 
    correct_answers += 1 

    # If input is incorrect, then print "Your answer is incorrect "
else : 
    print ("Your answer is incorrect...\n")

# Question 8

city_capital8 = (input("8. What is the capital of Spain? \n"))

# If input is correct 'madrid', then print "Your answer is correct "

# Insert the .lower() method which ignores any uppercase letters for the answer. 
if (city_capital8.lower() == ("madrid")):

    print ("Your answer is correct!\n") 
    correct_answers += 1 

    # If input is incorrect, then print "Your answer is incorrect "
else : 
    print ("Your answer is incorrect...\n")

# Question 9 

city_capital9 = (input("9. What is the capital of Sweden? \n"))

# If input is correct 'stockholm', then print "Your answer is correct "

# Insert the .lower() method which ignores any uppercase letters for the answer. 
if (city_capital9.lower() == ("stockholm")):

    print ("Your answer is correct!\n") 
    correct_answers += 1 

    # If input is incorrect, then print "Your answer is incorrect "
else : 
    print ("Your answer is incorrect...\n")

# Question 10 

city_capital10 = (input("10. What is the capital of Monaco? \n"))

# If input is correct 'monaco', then print "Your answer is correct "

# Insert the .lower() method which ignores any uppercase letters for the answer. 
if (city_capital10.lower() == ("monaco")):

    print ("Your answer is correct!\n") 
    correct_answers += 1 

    # If input is incorrect, then print "Your answer is incorrect "
else : 
    print ("Your answer is incorrect...\n")

# The score out of 10 

the_score_out_of_10 = correct_answers
print (f"Your total score is: {the_score_out_of_10}/10")


