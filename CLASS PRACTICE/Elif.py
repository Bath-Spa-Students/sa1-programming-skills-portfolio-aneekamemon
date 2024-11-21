#IF STATEMENT - ELIF (LECTURE 6-7)

a= 45
b= 167
if b > a:
    print("a is greater than b ")
elif a==b:
    print("a and b are equal")
else:
    print("b is greater than a ")

a=13
b=13
if a==b:
    print("a is equal to b")
else:
    print("a is not equal to b")


b=90
p=90
if b!=p:
    print("b isn't the same as p")
else:
    print("b is the same as p")




# Nested decision structures and the if-elif-else statement

salary = int (input("Enter your salary :"))
if salary >= 50000:
        years_on_job = float (input("Enter the years of job: "))
        if years_on_job >= 2:
            print ("You qualify for your job ")
        else: 
             print ("experience is less than 2 ")
else: 
        print ("you need to earn atleast 50 k to qualify ")
    

# ELIF

# Using nested decision structure to determine a grade

# Taking the graded score from the user (the input).
score = int(input("Enter your score :"))
if score >= 90: # Give the score input a value of 90 or above.
    # If the user input is 90 or above, print "your grade is an A"
    print ("your grade is an A.") 
elif score >= 80: # Give the score input a value of 80 or above.
    # If the user input is 80 or above, print "your grade is B"
    print ("your grade is B.")
elif score >= 70: # Give the score input a value of 70 or above.
    # If the user input is 70 or above, print "your grade is C"
    print ("your grade is C.")
elif score >= 60: # Give the score input a value of 60 or above.
    # If the user input is 60 or above, print "your grade is D"
    print ("your grade is D.")
if score <60: # Give the score input a value of below 60.
    # If the user input is below 60, print "your grade is F."
    print ("your grade is F.")
