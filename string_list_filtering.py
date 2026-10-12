
list = ["list","bat","apple","pear","the"]
#create a function to take in a list of strings and filter out the strings less than 4 characters 
#then output the list with the remaining strings in upper case
def filter(list):
    new_list = [i.upper() for i in list if len(i) > 3] #using list comprehension
    return(new_list)

print(filter(list))