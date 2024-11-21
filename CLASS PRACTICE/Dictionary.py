# Thursday 7th November 2024 

# A dictionary is a object that stores a collection of data which consists of a key and a value

# The format for creating a dictionary : dictionary = {key1: val1, key2:val2}.


# To add and place value in the dictionary

dictionary = {'color' : 'red' , 'fruit' : 'apple' , 'place' : 'UAE'}
print (dictionary['color'])

dictionary = {'color' : 'red' , 'fruit' : 'apple' , 'place' : 'UAE'}
print (dictionary['fruit'])

dictionary = {'color' : 'red' , 'fruit' : 'apple' , 'place' : 'UAE'}
print (dictionary['place'])

dictionary = { 'name' : 'Aneeka' , 'age' : '18' }
print (dictionary, 'name' (dictionary))

# Wednesday 13th November 2024


# To test '.items' methods...

dictionary  = { 'Name' : 'aneeka' , 'birth month ' :  'april' , 'University ': 'BSU' } 
print(dictionary.items())

# To test 'keys' in our dictionary...

dictionary  = { 'Name' : 'aneeka' , 'Birth Month ' :  'april' , 'University ': 'BSU' } 
print(dictionary.keys())

# Delete method - gets rid of value an/or keys

dictionary  = { 'Name' : 'aneeka' , 'Birth Month ' :  'april' , 'University ': 'BSU' } 
del dictionary ["Name"]
print(dictionary.items())

# The 'pop' method - removes specific dictionary 

dictionary  = { 'Name' : 'aneeka' ,
                'Birth Month ' :  'april' , 
                'University ': 'BSU' } 

print(dictionary.pop("Name"))
print(dictionary.keys())
print(dictionary.values())


# pop items - or delete items from the last value dictionary always return element in the from of tuple

dictionary  = { 'Name' : 'aneeka' ,
                'Birth Month ' :  'april' , 
                'University ': 'BSU' } 

print(dictionary.popitem())
print(dictionary.keys())
print(dictionary.values())
