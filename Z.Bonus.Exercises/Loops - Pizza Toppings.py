# Loops - Pizza Toppings:

'''

Loops- Pizza Toppings :

Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping.

Print a message saying you’ll add that topping to their pizza.

# This has been copied from the bonus exercise sheet.

'''


pizza_toppings_list = []    # This is where user input for pizza toppings will be stored.


while True:

        # Ask the user for the pizza toppings they'd like. Strip() allows for whitegaps
    pizza_toppings = input("\nPlease Enter a pizza topping you'd like to add onto your pizza.\n\n Or type in 'Quit' if you have finished adding in all toppings: ").strip()
    
    if pizza_toppings == ("quit"):  # This will stop asking for the entrance of more toppings and will 

        print ("\nThank you for adding your toppings to the pizza!\n\n")   


        print (f"\n\nHere is a list of your Pizza Toppings: {pizza_toppings_list}\n\n") 
            # This will show the user all the toppings they have added...

        break   # This will stop the loop 



    else:       

                # append. will keep adding all inputted pizza toppings onto the complied list of toppings.
        
        pizza_toppings_list.append(pizza_toppings)  # This is where the pizza toppings data will be stored "pizza_toppings_list = []".
        
        
        
        print (f"\n\n{pizza_toppings} has been added to your list of toppings!")
            # As soon as a topping is added this is the message that will show up. 
    
    if pizza_toppings:

        print ("\n\n The toppings you have chosen are: \n")   # This is a list that will show the user the toppings they have added beforehand.
        
        
        for pizza_toppings in pizza_toppings_list:
            
            print (f"{pizza_toppings}")     # This will show the name of the topping added.
    
    
    else: 


        print ("Please enter your pizza toppings!")     # If no input was made this is what will show up.

        

