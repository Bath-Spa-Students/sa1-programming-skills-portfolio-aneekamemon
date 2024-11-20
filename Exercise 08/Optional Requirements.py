# Simple Search - Optional Requirements



# Define the list filled with the 6 string names. 

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

specific_name_search = input("Enter the name you'd like to search for: ").strip().lower().upper() # This allows the user to type the name they are looking for, irrespective capitalization or lowercase lettering. 
found = False

for name in names:
    if name.lower() == specific_name_search.lower():
        found = True
        print (f"The name {specific_name_search.lower()} is on the list!") # This is what will be printed out.
        break 
if not found:
    print (f"The name '{specific_name_search.lower()}' is NOT on the list... ") # If the name is not found, this will print out.
