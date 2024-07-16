#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:57:07 2023
@author: data_scientist
on dell got on 07 dec 2023 Dove computers Nairobi for data science. thank the Lord for 2023
"""

"""
An object in python is like a TV remote (which you ca use to increase volume, change the channel, etc). also in python
when you assign a value to a variable you are making a object which in turn can have many functions or methods. eg a string value can
have an "upper(), or lower() function / method with in the object." You call a function or method by using the dot operator.



"""


# Started a while back on 10 June 2024 at online Moringa 35k kes today is 21 June 2024 (MnM BD), learning about strings


# these are some methods that work on strings

print(90 * "*")# this is for printing asterics (*) 90 times
print("Homer Simpson".endswith('Simpson'))
print("Charles Montgomery Burns".endswith('Simpson'))

# Let's ask Python for help with finding more information about what we can do with strings.

# help() function and it tells us everything it knows about that data type.
print()
print("Trying out STRING methods")
print()

course = "python is a fun course for beginners" # course is an STRING object with many fns or methods

print(course.capitalize()) #with the dot operator i can call any fn/method in the string object in this case i have called the capitalize() fn/method. which just makes the string upper case for the first letter like a sentence.
print(course.upper())
print(course.lower())
print("the index is ",course.find('f')) # the find() fn/method returns the index of the letter "f" in our string. it returns an error is the value we have specified does not exist in our string
print(course.find('for')) # the find() fn/method returns the index of the word "for" 

#print(course.replace('for',4)) # trying to replace "for" with 4 BUT it returned an error, this is because the replace() method only accepts strings not intergers or other data types
print(course.replace('for','4'))

a1="Dear lord jesus, can i get a scholarship. please. in jesus' name i pray. amen".title() # seem to out put captilizing the 1st letter of each word
print(a1)
num_to_string = 1234 # which is an int datatype
num_to_string = str(1234) # we hve converted this to a string data type
print(type(num_to_string)) # checking which datatype our variable is
print(num_to_string)

# it is only possible to concatenate two or more strings, same data type. It is not possible is one is an int and the other a string
full_address = num_to_string + " Abc street, Hometown USA"
print (full_address)

# replace method on a string
name1 = "Bart Simpson"
name2 = name1.replace("Simpson","Flanders")
print(name1)

# booleans answer whether something is True or False
# Every email address should end with ".com". Find the right string method to check if the email address ends with ".com" and return True or False accordingly.
# use the endswith("put the thing u wanna check here") method
ends_with_com = "art.vandelay@vandelay.co" # False
print(ends_with_com.endswith(".com"))


# reset variable to 0
vacation_days = 0

# this increments. notice the plus sign before the assignment
vacation_days += 1 # is the same as writing "vacation_days = vacation_days + 1"
vacation_days += 1

# print how many vacation days there are
print(vacation_days)

"""
The += is used to increment the current value of the variable and assign 
this new value back to it. The statement vacation_days += 1 can be 
thought of as vacation_days = vacation_days + 1. 
On line 1 we assign vacation_days the value 0. So, on line two, 
we reassign vacation_days to equal the current value of vacation_days, 
which is 0, plus 1. Again we increment vacation_days on line 3, 
which would now equate to 1 + 1, and finally we output the new value of vacation_days, 2.
"""
print()
print()
print("!**!**"*30)

# A block is any code that is grouped together. With conditionals, we indicate that something is part of the block by indentation. 
# To end the block we simply stop indenting.

# elif only follow another elif or if statement

# below program is for my practice of conditional statements.
# if we meet our FY target, we get a salary increase

salary_increase = 1000000 # current salary
fygoals_met = True # an example of how to use boolen
if fygoals_met:# only evaluates if TRUE never when it evaluates to FALSE
    # all code indented under the if statement is the block
    # indented code runs since conditional argument is True
    salary_increase += 50000
    print("New salary = ", salary_increase)
    print("we incremented our salary")
# if block ends

# introducing an else to our salary increase program

salary_increase = 1000000 # current salary
fygoals_met = False # an example of how to use boolen
if fygoals_met:# only evaluates if TRUE never when it evaluates to FALSE
    # all code indented under the if statement is the block
    # indented code runs since conditional argument is True
    salary_increase += 50000
    print("New salary = ", salary_increase)
    print("we incremented our salary")
# if block ends
else:
    # else block start
    print("****************")
    print("Sorry team, No increase because you did not meet the target, try again next FY")
# else block ends
#program ends

print("*******&&&&&&&&&&&&&&&&&&&*********")
# introducing the elif.
# our code now shall check is we met or exceeded the target

salary_increase = 1000000 # current salary
fygoals_met = False # an example of how to use boolen
fytarget_exceed=True
if fygoals_met:# only evaluates if TRUE never when it evaluates to FALSE
    # all code indented under the if statement is the block
    # indented code runs since conditional argument is True
    salary_increase += 50000
    print("New salary = ", salary_increase)
    print("we incremented our salary")
# if block ends
elif fytarget_exceed:
    print("Congratulations you exceeded the target. surplus.")
    print("Here is your 13th cheque: ", salary_increase*2)
    
else:
    # else block start
    print("****************")
    print("Sorry team, No increase because you did not meet the target, try again next FY")
# else block ends
#program ends


# what is falsy in Python? Zero is falsy, and None is falsy. Also falsy are values like empty strings ("") and empty lists ([]),

vacation_days = 1
if vacation_days: # evaluates as True bacause the initial value is not am empty string/list/a Zero or None value
    # this is run
    vacation_days += 1
print(vacation_days)

vacation_days = 0
if vacation_days: #since the initial value is Zero, thsi evaluates as a false, so the condition block shall not execute.
    # this is not run
    vacation_days += 1
print(vacation_days)

# another falsy type code
greeting = ''
if greeting:
    greeting += 'Hello'
else:
    greeting += 'Goodbye'
print(greeting)

# If we are ever curious about the whether something is truthy or falsy in Python, we can just ask with the bool function.

bool(0) # False
bool(1) # True
bool('')
bool([])

print("Important info about boolean, True is set to 1 while Falze is set to 0. so you can perform math operations on them")
a=True+4+5+True # answer should be 11
print()
print()
print(a)
print(True+False) # answer should be 1

# Boolean values (True and False) can also be used in mathematical equations. True is set to 1 and False is set to 0.

# example of using boolean and endswith string method to check if a word ends with certain specified letters.

string = "Python"
sub_string = "on"
ends_with = None
if string.endswith("on"):
  ends_with = True
  print(ends_with)
else:
  ends_with = False
  print(ends_with)
# conditionals go here

wizard_list1 = ['spider legs','toe of frog','eye of newt','bat wing','slug butter','snake dandruff']
print(wizard_list1)

# to add anything in a list we can use the append method.
# NB: methods use normal brackets when calling them

# wizard_list1.append["lion teeth"] # made a mistake when working on the list by calling the append method using [] instead of (). it returned an error and i corrected it below

wizard_list1.append("lion teeth")
wizard_list1.append("monkey teeth")
wizard_list1.append("horse hair")
print(wizard_list1)

# we can use the pop method to remove items from a list
wizard_list1.pop() # by default this removes the last item but we can specify which item to remove by using its index

print(wizard_list1)
print(len(wizard_list1))
wizard_list1.pop(2) # removing the 3rd item
print(wizard_list1)
# or use the 'del' function to delete items
del wizard_list1[2]
print(wizard_list1)
print(len(wizard_list1))

wizard_list1.append("lion teeth")
wizard_list1.append("monkey teeth")
wizard_list1.append("horse hair")

print()
print()

print(wizard_list1)

print()
print()

# sets and lists
# A list is our first form of a collection. A collection is just a way of grouping multiple pieces of data together.
"""
Well to see a unique list of the elements, we can call the set function. 
A set is a different type collection in Python. A set is just like a list, except elements do not have order and each element appears just once.
"""
 # this makes our list a SET (data type). 
# set only has unique elements and is STB unordered because it re arranges the indexes and elements seem to be arranged in alphabetical order.
# Lists are ordered because each element has an index
unique_wizard_list1=set(wizard_list1)
print(unique_wizard_list1)

# python developers prefer to work with lists as opposed to sets, as lists are generally easier to manipulate because they are ordered/indexed

# Lists use indexes to locate elements in the list. while dictionaries use labels/names/titles to locate elements in the dictionary.
# lists use [] braces, tuples use () braces, dictionaries use {} braces, Sets also to use {}
# dictionaries are represent attributes of an entity such as the various attributes of a single TV show like its name, genre, starring actors, etc.
# Dictionaries are collections of key-value pairs.
# DICTIONARIES are like a table with "table column headings" (KEYS) and each column has the values or data (VALUES)
# "table column headings" (KEYS) are the attributes we want for our table/entity
# Rather then specifying a positional index as with lists, we specify a key for a dictionary and are returned with the value associated with that key.

# retrieving for LISTS (list_name[index nbr])and DICTIONARIES dict_name['key_name']
# This is similar to traditional dictionaries: you look up a specific word (the key) to find its associated definition (the value).

print('******************************************************************************************************************')
print()
print()

print('*!*!*!*'*2, 'HERE My try on LISTS and DICTIONARIES also known as MAPS','*!*!*'*2)
print()
# A list can be a list of cars you love
# mycars=("Land rover","Nissan Patrol",'Mercedez', 'Bentley','BMW', 'VW',"FJ Cruiser") # this is a mistake because a list used [] not () here i would be better off making it a string list
mycars=["Land rover","Nissan Patrol",'Mercedes', 'Bentley','BMW', 'VW',"FJ Cruiser"] #lists use [] braces

print(mycars)
print(len(mycars))
mycars.append("added car")
print(mycars)

# for a dictionary you can use to decribe what your fav cars specs are

# LR_dict={'model':"LR Discovery4",'YoM':2024,'make':"Land Rover"}

# let me try to creat a list of each fav car

Classic_LR=['Discovery 1', 'Discovery 2','Discovery 3','Discovery 4','LR Sport']
Defender= ['Defender 130','Defender 110', 'Defender 90']
Range_rover=['Velar','Evoque','RR Sport']

land_rover=[Classic_LR, Defender, Range_rover] # list of LR makes
print(land_rover)


LR_dict={'Land Rover models':land_rover,'Nissan Patrol models':['Y60','Y61','Y62'],'Mercedes models':['W126','E-class','SE-Class'], }
# if i wanted to access RR sport
# first access the 'KEY or ATTRIBUTE' in the dictionary then its value
LR_dict['Land Rover models'] # retrieving for DICTIONARIES dict_name['key_name'] while for LISTS (list_name[index nbr])

# Bt for our dictionary the value of the KEY is in a LIST and to access elements in a list we "list_name[index number]"

print(LR_dict['Land Rover models'][-1][-1])

import pandas as pd
brics = pd.DataFrame(LR_dict)
print(brics)

print()

print()
print('Lists and tuples')
# lists use [] braces, tuples use () braces, dictionaries use {} braces, Sets also to use {}
# if you creat a variable and assign values (string or numbers) with out put any braces/brackets it becomes a TUPLE. confirm by checking type('variable name')
# the difference between a TUPLE & a LIST is that a tuple values can not be changed/updated NB: the valriable can point to somthing else if your RE-assign it BUT the elements inside a TUPLE
# shall remain the same once you create it.
# the moment you put a coma after the first variable ...without using braces from the start of the assignment, then you are making a TUPLE
t1=1,'two','many',908,'3edw' # this is a TUPLE
print(t1)
print(type(t1))
print()
print('deleting or adding or updating the items in the list we have just created above---BRINGS ERROR')
# deleting or adding or updating the items in the list we have just created above
print('printing the 3rd item/element in our TUPLE:  ',t1[2]) 
print(t1)
print()
print('Updating/deleting the 3rd item/element in our TUPLE:  ')
# t1[2]='TIP TIP TIP' # brings an error because 'tuple' object does not support item assignment

# del t1[2] # brings an error because 'tuple' object does not support item deletion

# t1.append('another item in out tuple') # brings an error because 'tuple' object has no attribute 'append'

print(t1)
print()
t2=1,2,4,5,6,7,67 # this is also a TUPLE
print(t2)
print(type(t2))
print()
t3=(1,5,8876,232,'cars','83ue','many times', "friends",13213) # this is also a TUPLE
print(t3)
print(type(t3))

'''
Why would you use a tuple instead of a list? Basically because
sometimes it is useful to use something that you know can never
change. If you create a tuple with two elements inside, it will
always have those two elements inside.

'''

# MAPS aka DICTIONARIES a map (each key maps to a particular value)
# the Map/dictionary below is of my home people and their favorite things
fav_things = {'MnM' : 'Chickens',
'John Bosco' : 'Liverpool',
'Elain in Canada' : 'Having fun',
'Ciara' : 'Laughing at jokes',
'Mein kempf' : ('Cartoons','F1','Messi','Barca','Python','Family','photograpy','travel'), # the value for this key is a TUPLE
'Tatiana Ali' : 'Wrestling WWE',
'Rosman':'Law',
'Jayz Jakes':'Cartoons',
'Lil*R':'Nigeria Movies',
'Lil Lion':'Bluey'
}
print()
print()
print()
print(fav_things)

jayfavs=['Cartoons','Movies','Driving','Telecom',"Cars"] # here and trying to create a list of Jayz Jakes ' favs in a list and update the dictionary 

fav_things = {'MnM' : 'Chickens',
'John Bosco' : 'Liverpool',
'Elain in Canada' : 'Having fun',
'Ciara' : 'Laughing at jokes',
'Mein kempf' : ('Cartoons','F1','Messi','Barca','Python','Family','photograpy','travel'), # TUPLE ()
'Tatiana Ali' : 'Wrestling WWE',
'Rosman':'Law',
'Jayz Jakes':jayfavs, # this has updated and the value is pointing to a LIST []
'Lil*R':'Nigeria Movies',
'Lil Lion':'Bluey'
}

print()
print()
print()
print(fav_things)

# accessing items in our created dictionary

print()
print(fav_things['Rosman'])
print(fav_things['Jayz Jakes'])
print()
print()
print(type(fav_things['Mein kempf']))
print(type(fav_things['Jayz Jakes']))


# first group discussion code with Stephen Muny, Allan kimath, Anthony Manyura, and Kago
nbr1=4
nbr2=5
nbr3=3
if nbr1==1:
    print("one")
elif nbr2==2:
    print("two")
else:
    print("three")

# we can use a library called Pandas to get data from an excel file or other source into our Python code.
# 
'''
Note: To import a library or module in Python, we do so by writing import followed 
by the name of the thing we want to import. 
We can optionally include an alias for our import, which is done by writing as 
after the name of the thing we are importing followed by the name we would 
like to use for our alias. Do not worry about aliases right now. 
Just know that the convention for importing the Pandas library is to import 
it and alias it as pd like we see below.


Pandas is a great tool when trying to accomplish a task such as turning data 
from an excel file into data we can use in Python.
'''

# Run this cell without changes
import json
with open("coffee_product_reviews.json") as f:
    reviews = json.load(f)
type(reviews)

num_reviews = None
print(reviews)

'''
A for loop essentially has two necessary components, which we'll refer to as 
arguments. The first argument is the variable name we are assigning to an 
element, or in this case, number. The second argument is the collection we are 
iterating over, or in this case, the list zero_to_three.

'''

print()
print('X*X*'*25)
print()
print("Studying the FOR LOOP")
print('*'*30)

#n_index=0

zero_to_three=[2,49,99,21]

n=0 # creating a variable for the 1st position / index of the 1st element in our list
for anynbr in zero_to_three:
    #n_index=len(zero_to_three)
    
    # A for loop essentially has two necessary components: the iterating variable and the object/collection we are looping /iterating through.
    print(anynbr,'index position in our list is ',n)
    n=n+1 # as the loop goes through our list its increases n by 1 to plot the index number
    #a=n_index
    #print(anynbr, ' is the ',a, ' element')
    
    #print(n_index)
    #print(len(zero_to_three))
    #print(anynbr, ' is in index position ', zero_to_three.index(n_index))
    #n_index=n_index+1

print('*'*30)


"""
# trying to make this for loop work. i want it to print the number in the list and also indicate its index
# finally made it work up example. am keeping this code to see where i was making a mistake.

n_index=0
#zero_to_three=[0,1,2,3]
zero_to_three2=['zero','one','two','three']

for anynbr in zero_to_three2:
    ''' A for loop essentially has two necessary components: the iterating variable 
    and the object were are looping /iterating through.'''
    print(anynbr,' is in index position ', zero_to_three2.index(n_index))
    n_index=n_index+1
    #print(anynbr, ' is in index position ', zero_to_three2.index(n_index))
    

print('*'*30)

"""
# Using list elements as indices to access elements in another list
countries = ['Croatia', 'USA', 'Argentina', 'France', 'Brazil', 'Japan', 'Vietnam']
cities = ['Zagreb', 'District of Columbia', 'Buenos Aires', 'Paris', 'Rio de Janeiro', 'Tokyo', 'Hanoi']
for index in [0,1,2,3,4,5,6]:
    #print(index)
    print(countries[index],' index position is ', index)

print()
print('*'*30)
print('Printing the countries and the cities so they list on the same line')
print()
for index in [0,1,2,3,4,5,6]: # Of course, this does not work if our indices do not match up with the length of our list.
    print(cities[index]+",", countries[index])

# if u donot know the length of the list, u can use the range function
a1=range(0,len(countries))

print()
print('Using RANGE Class to create a list of numbers')
print()
for index in a1:
    print(cities[index]+",", countries[index])

print()
print('USING THE ENUMERATE METHOD')
print()
for idx, item in enumerate(cities):
#for idx, item in enumerate(['A', 'B', 'C']):
    print(idx, item)
    #print(item, idx)
print()
print()
# we can iterate through a list that contains multiple data types
different_elements = ['A String', ["a", 'list', "of", 5, ["elements"]], {'this': "is a dictionary"}]
for element in different_elements:
    print(element)

# in Python, we can't iterate directly over the dictionary, we iterate over the items of a dictionary, which are the key-value pairs.

print()
print()
print('iterating over A DICTIONARY ITEMS')
print()
# LETS USE our fav_things dictionary we created earlier
print(fav_things.items()) # the items() method puts our dictionary key/value pair in a list like format, which makes it easier to iterate over

print()
for ky,vl in fav_things.items():
    print(ky,':',vl)


print()
ice_cream_flavors = ['Mint Chocolate Chip', 'Coffee', 'Cookie Dough', 'Fudge Mint Brownie', 'Vanilla Bean']
for ice_cream_flavor in ice_cream_flavors:
    print('I love ' + ice_cream_flavor + ' ice cream!!')

# ********************it 06 July 2024 1750hrs, same lesson as loops am doing on "otherloops.py"************
# but the exercise has some dictionary to iterate over so i had to put the code exercise in this file

# QN: Use a for loop to find the first person in the list of people that has a dog as their pet. The iteration count shouldn't exceed 2.
print()
print()
print('***************************************************')
people = [
    {'name': "Daniel", 'age': 29, 'job': "Engineer", 'pet': "Cat", 'pet_name': "Gato"},
    {'name': "Katie", 'age': 30, 'job': "Teacher", 'pet': "Dog", 'pet_name': "Frank"},
    {'name': "Owen", 'age': 26, 'job': "Sales person", 'pet': "Cat", 'pet_name': "Cosmo"},
    {'name': "Josh", 'age': 22, 'job': "Student", 'pet': "Cat", 'pet_name': "Chat"},
    {'name': "Estelle", 'age': 35, 'job': "French Diplomat", 'pet': "Dog", 'pet_name': "Gabby"},
    {'name': "Gustav", 'age': 24, 'job': "Brewer", 'pet': "Dog", 'pet_name': "Helen"}
]


# my attempt at answering the qn above to find the person whose per is a dog
first_dog_person = None
iteration_count = 0
for person in people:
    iteration_count += 1
    that_person=person.items()
    for ky,vl in that_person: # Basically what happens with a nested loop is the inner loop runs in its entirety every iteration of the outer loop
      if vl=="Dog":
          
          print(that_person) # so far the program has printed All those with a dog as a pet. good start. i want it to print only the first person not all
          break
          # continue
          #print(ky,":",vl)
          # break
print('----------------------')  
for person in people:
    for pets in person['pet']:
        print(pets)
      # if pets=="Dog":
      #     print(person)
      #     break

print()
print()
print('***************************************************')
# Today is 07 July 2024 its about 14:47hrs

# In my solution above about printing only the first person with a pet as a dog, the inner FOR loop is printing all those with a pet as a dog
# let me study this further

# Basically what happens with a nested loop is the inner loop runs in its entirety every iteration of the outer loop. See example below.

outer_numbers = [1,2,3]
inner_words = ["ONE", "TWO", "THREE"]
for number in outer_numbers:
    print(f"this is iteration **{number}** of the OUTER loop")
    for word in inner_words:
        print(f"     this is iteration {word} of the INNER loop")
    print("\n")
    
# another example of what happens with nested loops, the nested loop has to finish before the next iteration of the outer loop.  
print('----------------------') 
outer = 0
inner = 0
while outer < 3:
    outer += 1
    print("outer iteration:", outer)
    while inner < 3:
        inner += 1
        print("    inner iteration:", inner)
    inner = 0
    print("\n") 
   
# another example of what happens with nested loops, the nested loop has to finish before the next iteration of the outer loop.     
print('----------------------')    
    
programmers = [{'name': "rachel", 'favorite_languages': ['Ruby', 'JavaScript', 'SQL', "Java"]},
               {'name': "daniel", 'favorite_languages': ['JavaScript', 'Elixir', 'Python']},
               {'name': "greg", 'favorite_languages': ['C#', 'CoffeeScript', 'R']},
               {'name': "meryl", 'favorite_languages': ['C++', 'PHP', 'Swift']}
              ]   
# if we wanted to take the above list of programmers and dynamically list out everyone's favorite_languages we would need to use two separate loops.    
for programmer in programmers:
    for language in programmer['favorite_languages']:
        print(language)
        



print()
print()
print('**********************STUDYING FUNCTIONS*****************************')
# FUNCTIONS give us the ability to name a sequence of operations (or block of code)
new_employees = ['jim', 'tracy', 'lisa']

# We want to send each of them a nice welcome message. We could use a for loop to create a list of welcome_messages.
welcome_messages = []
for new_employee in new_employees:
    welcome_messages.append("Hi " + new_employee.title() + ", I'm so glad to be working with you!" )

print(welcome_messages)


# FUNCTIONS give us the ability to name a sequence of code/a code block.
print("Our greeting function")
def greet_employees():
    welcome_messages = []
    for new_employee in new_employees:
        welcome_messages.append("Hi " + new_employee.title() + ", I'm so glad to be working with you!" )

    return welcome_messages # storing what the fuctions has done without printing/outputing the contents.
print(greet_employees()) # calling the function to print whats inside it



# create an function that iterates over LISTS, DICTIONARIES


def find_the_mean(list_nums):
    length = len(list_nums)
    total = sum(list_nums)
    return total/length

find_the_mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

area_one_pops = [10453, 12383, 8034, 800835, 76434, 32394]
find_the_mean(area_one_pops)


area_two_pops = [43845, 54930, 59354, 96403, 73492, 729320]
find_the_mean(area_two_pops)
def find_biggest_pop(list_pops_one, list_pops_two):
    mean_one = find_the_mean(list_pops_one)
    mean_two = find_the_mean(list_pops_two)
    if (mean_one > mean_two):
        return print("The first list,", list_pops_one ," has the larger mean population")
    else:
        return print("The second list,", list_pops_two ,"has the larger mean population")
find_biggest_pop(area_one_pops, area_two_pops)  

# today 08 july 2024 class on pandas. here trying to attempt the lab on accessing data with pandas, here trying to put a condition to access some data.

import pandas as pd

data = {'set_of_numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

df.loc[df['set_of_numbers'] <= 4, 'equal_or_lower_than_4?'] = 'Yes' 
df.loc[df['set_of_numbers'] > 4, 'equal_or_lower_than_4?'] = 'No' 

print(df)  


# date is 09 July 2024 2028hrs.
# i wanna try to create a function(s) that adds numbers from a list, input by user, and static nbrs. from both empty functions and those that take arguments

print()
print()
print('----------------------------------------------09 July 2024----------------------------------------------')

list_of_nbrs=[1,2,3,4,5,6,7,8,9,10,0,12]
print(len(list_of_nbrs))
print(type(list_of_nbrs))
print(list_of_nbrs[3])
print(list_of_nbrs[9])
print(list_of_nbrs[9]-list_of_nbrs[3])

print('-----'*5)
adds_list=0 # initializing the first addition


for numbr in list_of_nbrs: # this piece of code adds the numbers in a list
    adds_list=adds_list+numbr
print(adds_list)


print('------END--------')
# creating a function that does the same thing above
print()
print('-----'*5)
print('this my function for adding numbers/elements in a list')



def adding_function(list_of_nbrs):
    adds_list1 = 0 # initializing the first addition
    for numbr1 in list_of_nbrs:        # this piece of code adds the numbers in a list
        adds_list1 = adds_list1 + numbr1
    return adds_list1
print('-----'*5)
print(f'The answer of adding function is: {adding_function(list_of_nbrs)}')
print('-----'*5)
# additions=adding_function(list_of_nbrs)
# print(additions)
# the return statement is used to keep/return a value which you can in turn store in another variable
# Note: Return statement can not be used outside the function.
# The return statement in Python is used to exit a function and return a value to the caller.
        #print(adds_list1) # this has not worked
#print(adds_list1)





#adding_function(adds_list1) # did not work
print('adding_function answer is supposed to be here')

# IMPORTANT: there are 2 types of functions 
# (1) that does a task and 
# (2) one that returns a value

print()


print("----------------a function that does a task---------------------")
def greets(name): # this functions just does a task
    print(f'Habari, {name}') # this function's task is to print a greeting
greets("Moringa students")
greets('data science students')

print()


print("----------------a function that returns a value-----------------")
def greets2(name):
    return f'Habari brother/sister - {name} '
# this one that returns a value allows one to get this value and store it in a variable. like this
messages=greets2('Ntare')
print(messages)


print()
print('----------------------------END-----------------------')
print()

a=30
b=20
c=12
# print(a+b+c)

def addings1(a,b,c):
    add_answer1=a+b+c
    return add_answer1


print('-----'*5)






















    