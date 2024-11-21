# Wed 6th November 2024 

# The 'while' loop: a condition-controlled loop. 

# This is a loop that prints numbers below 10, after which it stops...

i = 1

while i < 10:
    print (i)
    i += 1 


# This is a loop that breaks up if a certain input is added

j = 1
while j < 6:
    print (j)
    if j == 3:
        break 
    j += 1;                 # j = j + 1 (both are the same)


# The 'for' loop 

# Using the range function with the for loop 

# This code extracts the '2' times table between the ranges 0 - 20 

for x in range (0,20,2):
        print (x, end= " ")


# This code extracts the '5' times table between the ranges 0 - 50

for x in range (0,50,5):
        print (x, end= " ")


for x in range (10):
     print (x)


# Getting an input from user -  (User Controlled Loop)

N= int (input("Enter max number for range :"))
for x in range (0, N ,5):
      print(x,end=" ")
