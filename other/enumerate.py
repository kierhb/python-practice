'''
    What if you want to access the elements in a list, along with the index of the element in question? 
    You can do this using the enumerate() function. The enumerate() function takes a list as a parameter 
    and returns a tuple for each element in the list. The first value of the tuple is the index and the 
    second value is the element itself.
'''

def details(people):
    accounts = []
    for index, name in enumerate(people):
        accounts.append(f"{name} - < {index + 1} >")
    return accounts


print(details(["Alex Diego", "Shay Brandt"]))
