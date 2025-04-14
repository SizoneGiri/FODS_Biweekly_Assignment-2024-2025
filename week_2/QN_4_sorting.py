'''A program to accept a list of names and return the sorted order of names back.'''

#function to sort the list
def Sort_names (name):
    lst= name.split(",") #turns the string into a list
    lst= [name.strip() for name in lst] #removes the whitespaces and \n
    lst=sorted(lst)#sorts the list
    return lst #returns the sorted list

#input from the user
Names= input ("Enter names separated by commas : ")
#displays the output
print(Sort_names(Names))