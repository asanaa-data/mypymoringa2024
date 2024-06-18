#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:57:07 2023
@author: data_scientist
on dell got on 07 dec 2023 Dove computers Nairobi for data science. thank the Lord for 2023
"""

a=4
b=11
c=12
d=23
e=b-a
print(b)
print(e)
print(d-b)
print("the answer is:",e)
print("the answer is: ",d*b)
a*a
e/b

# studying python for beginners by programming by Mosh

dd=print("the fat answer is: ",d*b) #trying to assign the value of the print fn to a variable. to store the value of the print fn.
dd

#receiving input from a user. we use the "input" fn
name=input("What is your name: ")
age=input("How old are you: ")
print(name, " is " ,age, "years old" )

# program to add two or more numbers
firstnbr=int(input("enter 1st nbr: "))# the input fn returns a string even if you enter a number. so here I converted the input value from string to interger
secondnbr=float(input("enter 2nd nbr: ")) # the input fn returns a string even if you enter a number. so here I converted the input value from string to float
adds=print("answer is: ", firstnbr+secondnbr)
adds


"""
An object in python is like a TV remote (which you ca use to increase volume, change the channel, etc). also in python
when you assign a value to a variable you are making a object which in turn can have many functions or methods. eg a string value can
have an "upper(), or lower() function / method with in the object." You call a function or method by using the dot operator.



"""
course = "python is a fun course for beginners" # course is an STRING object with many fns or methods
course.capitalize() #with the dot operator i can call any fn/method in the string object in this case i have called the capitalize() fn/method. which just makes the string upper case for the first letter like a sentence.
print(course.upper())
print(course.lower())
print("the index is ",course.find('f')) # the find() fn/method returns the index of the letter "f" in our string. it returns an error is the value we have specified does not exist in our string
print(course.find('for')) # the find() fn/method returns the index of the word "for" 

#print(course.replace('for',4)) # trying to replace "for" with 4 BUT it returned an error, this is because the replace() method only accepts strings not intergers or other data types
print(course.replace('for','4'))











