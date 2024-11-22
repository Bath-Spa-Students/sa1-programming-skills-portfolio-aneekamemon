# Simple Search - Optional Requirements

'''
Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.
# This has been copied from the exercise sheet.
'''

# Define the list with the 6 string names. 

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

specific_name_search = input("Enter the name you'd like to search for: ").strip().lower().upper() # This allows the user to type the name they are looking for, irrespective capitalization or lowercase lettering. 

found = False

for name in names:



    if name.lower() == (specific_name_search.strip().lower()):
        
        
        print (f"The name {specific_name_search.strip().lower()} is on the list!") # This is what will be printed out.
        
        break 

    
else:
    
    print (f"The name '{specific_name_search.strip().lower()}' is NOT on the list... ") # If the name is not found, this will print out.
