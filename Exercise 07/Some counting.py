# Some counting 

'''

Use your newly acquired knowledge of the for loop to complete the following
tasks. Print all values to the console in each case. * Write a loop that counts
up from 0 to 50 in increments of 1. * Write a loop that counts down from 50 to
0 in decrements of 1. * Write a loop that counts up from 30 to 50 in increments
of 1. * Write a loop that counts down from 50 to 10 in decrements of 2. * Write
a loop that counts up from 100 to 200 in increments of 5. You may include all
loops in a single project

# This has been copied from the exercise sheet.
'''

print ("Counting up from 0 - 50: \n" )     # This loop counts upwards from 0 to 50 with the increments of 1. The \n allows for a gap. 

for thenumbers in range (0, 51, 1):
    print (thenumbers)

print ("\n Counting down from 50 - 0: \n")     # This loop counts downwards from 50 to 0 with the increments of 1
#The \n allows for a gap. 
for thenumbers in range (50, -1, -1):
    print (thenumbers)

print ("\n Counting up from 30 - 50: \n")     # This loop counts upwards from 30 to 50 with the increments of 1
#The \n allows for a gap. 
for thenumbers in range (30, 51, 1):
    print (thenumbers)

print ("\n Counting down from 50 - 10: \n")     # This loop counts downwards from 50 to 10 with the increments of 2
#The \n allows for a gap. 
for thenumbers in range (50, 9, -2):
    print (thenumbers)

print ("\n Counting up from 100 - 200: \n")     # This loop counts upwards from 100 to 200 with the increments of 5
#The \n allows for a gap. 
for thenumbers in range (100, 201, 5):
    print (thenumbers)
