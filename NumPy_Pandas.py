#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:02:29 2024

@author: data_scientist
"""

# Today 12 July 2024, studyinn NumPy and Pandas
# NumPy also provides us with fast and efficient, list-like, 
# data types called N-Dimensional Arrays or ndarrays or more simply arrays.
# An important note: Pandas was actually built on top of NumPy! 
# So many of the functionalities that NumPy has, are also part of Pandas. 

# NumPy (Numerical Python) is an open source Python library.
# The NumPy library contains multidimensional array data structures such as the homogeneous, N-dimensional
#  and NumPy has a large library of functions that operate efficiently on these data structures.
# Why NumPy: NumPy shines when there are large quantities of “homogeneous” (same-type) data to be processed on the CPU.
# NumPy is used to work with arrays. The array object in NumPy is called ndarray.
# We can create a NumPy ndarray object by using the array() function.
# 
# NumPy is one of the main libraries for performing scientific computing in Python. so there are others. but we shall focus on numpy
# 
# 

'''
an array is a structure for storing and retrieving data.

Most NumPy arrays have some restrictions. For instance:
    
    All elements of the array must be of the same type of data.(homogeneous**)
    Once created, the total size of the the array can’t change.
    The shape must be “rectangular”, not “jagged”; e.g., each row of a two-dimensional array must have the same number of columns.

**Python lists are excellent, general-purpose containers. 
They can be “heterogeneous”, meaning that they can contain elements of a variety of types,
'''
# One way to initialize an array is using a Python sequence, such as a list. For example

# first import the NumPy library
import numpy as np

# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

a = np.array([1, 2, 3, 4, 5, 6]) # # this is 1-D array or An array that has 0-D arrays as its elements

print(a) # this is 1-D or )-D array
print(f'array "a" is a : {type(a)}')
print(a.shape)
# Get the data type of an array object
print(a.dtype)
# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(f'This is a {a.ndim}-D array')
print("-----------------------------------------")

# the array element can be one element like below example variable (b)

# Create a 0-D array with value 42
b=np.array(42) # 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

print(b)
print(f'array "b" is a : {type(b)}')
print(b.shape) # note the difference on this output it is returning an empty shape
# Get the data type of an array object
print(b.dtype)
# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(f'This is a {b.ndim}-D array')
print("-----------------------------------------")


# but anything more than one element i.e a sequesnce has to be within brackets () or [] or {}
c=np.array((1,2,3)) # this is 1-D array or An array that has 0-D arrays as its elements

print(c)
print(f'array "c" is a : {type(c)}')
print(c.shape)
# Get the data type of an array object
print(c.dtype)
# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(f'This is a {a.ndim}-D array')
# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(f'This is a {c.ndim}-D array')
print("-----------------------------------------")



d=np.array({1,2,3}) # this is 1-D array or An array that has 0-D arrays as its elements

print(d)
print(f'array "d" is a : {type(d)}')
print(d.shape) # note the difference on this output it is returning an empty shape for the set (data structure that contains an unordered collection of unique values.)
# Get the data type of an array object
print(d.dtype)
# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(f'This is a {d.ndim}-D array')
print("-----------------------------------------")


cars={'make':'Nissan','model':'Patrol Y60','type':'SUV','color':'blue'} # this is 1-D array or An array that has 0-D arrays as its elements

e=np.array(cars)
print(e) # this is 1-D or )-D array
print(f'array "e" is a : {type(e)}')
print(e.shape) # note the difference on this output it is returning an empty shape for this dictionary

# Get the data type of an array object
print(e.dtype)
# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(f'This is a {e.ndim}-D array')
print("-----------------------------------------")


f = np.array(['one','two','three','four']) # this is 1-D array or An array that has 0-D arrays as its elements

print(f) # this is 1-D or )-D array
print(f'array "f" is a : {type(f)}')
print(f.shape)
# Get the data type of an array object
print(f.dtype)
# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(f'This is a {f.ndim}-D array')
print("-----------------------------------------")


# An array that has 1-D arrays as its elements is called a 2-D array.
# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6

g = np.array([[1, 2, 3], [4, 5, 6]])  # this is 2-D or An array that has 1-D arrays as its elements

print(g) # this is 1-D or )-D array
print(f'array "g" is a : {type(g)}')
print(g.shape)
# Get the data type of an array object
print(g.dtype)
# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(f'This is a {g.ndim}-D array')
print("-----------------------------------------")

g1 = np.array([[1, 2], [4, 5],[6, 7]])  # this is 2-D or An array that has 1-D arrays as its elements

print(g1) # this is 1-D or )-D array
print(f'array "g1" is a : {type(g1)}')
print(g1.shape)
# Get the data type of an array object
print(g1.dtype)
# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(f'This is a {g1.ndim}-D array')
print("-----------------------------------------")

g2 = np.array([ [[1, 2], [4, 5],[6, 7],[12,43]] ] )

print(g2) # this is 1-D or )-D array
print(f'array "g2" is a : {type(g2)}')
print(g2.shape)
# Get the data type of an array object
print(g2.dtype)
# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(f'This is a {g2.ndim}-D array')
print("-----------------------------------------")


# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6

h = np.array([ [[1, 2, 3], [4, 5, 6] ], [[1, 2, 3], [4, 5, 6] ] ])  # this is 3-D or An array that has 2-D arrays as its elements

print(h) # this is 1-D or )-D array
print(f'array "h" is a : {type(h)}')
print(h.shape)
# Get the data type of an array object
print(h.dtype)
# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(f'This is a {h.ndim}-D array')
print("-----------------------------------------")


# converting a list of temperature reading from Fahrenheit to Celsius using the formula : T(°C) = (T(°F) - 32) × 5/9
# Average temps in NYC from January -> December (in fahrenheit)
nyc_avg_temps_f = [39, 42, 50, 62, 72, 80, 85, 84, 76, 65, 54, 44]

# ----- Without NumPy -----
nyc_avg_temps_c = list(range(0,12))
nyc_avg_temps_c[0] = (nyc_avg_temps_f[0] - 32) * (5/9)
nyc_avg_temps_c[1] = (nyc_avg_temps_f[1] - 32) * (5/9)
nyc_avg_temps_c[2] = (nyc_avg_temps_f[2] - 32) * (5/9)
nyc_avg_temps_c[3] = (nyc_avg_temps_f[3] - 32) * (5/9)
nyc_avg_temps_c[4] = (nyc_avg_temps_f[4] - 32) * (5/9)
nyc_avg_temps_c[5] = (nyc_avg_temps_f[5] - 32) * (5/9)
nyc_avg_temps_c[6] = (nyc_avg_temps_f[6] - 32) * (5/9)
nyc_avg_temps_c[7] = (nyc_avg_temps_f[7] - 32) * (5/9)
nyc_avg_temps_c[8] = (nyc_avg_temps_f[8] - 32) * (5/9)
nyc_avg_temps_c[9] = (nyc_avg_temps_f[9] - 32) * (5/9)
nyc_avg_temps_c[10] = (nyc_avg_temps_f[10] - 32) * (5/9)
nyc_avg_temps_c[11] = (nyc_avg_temps_f[11] - 32) * (5/9)
# -------------------------

# ------ With NumPy -------
np_nyc_avg_temps_f = np.array(nyc_avg_temps_f)
np_nyc_avg_temps_c = (np_nyc_avg_temps_f - 32) * (5/9)
# -------------------------

print('1. Without NumPy:', nyc_avg_temps_c)
print("-----------------------------------------")
print('2. With NumPy:', np_nyc_avg_temps_c)

print()
print("-----------------------------------------")
# time difference between how long it takes us to perform the same operation with and without NumPy.

import time

# Using 1 million integers
huge_list_of_integers = list(range(0, 1000000))
huge_np_array_of_integers = np.array(huge_list_of_integers)

def add_one(list_of_ints):
    return [num + 1 for num in list_of_ints]


start_time = time.perf_counter() # Time when operation starts
add_one(huge_list_of_integers) # Adds 1 to each number in the list of integers above
end_time = time.perf_counter() # Time when operation finishes
total_time = (end_time - start_time) # Total time for operation


start_time_with_np = time.perf_counter() # Time when operation starts
huge_np_array_of_integers + 1 # Adds 1 to each number in the array of integers
end_time_with_np = time.perf_counter() # Time when operation finishes
total_time_with_np = (end_time_with_np - start_time_with_np) # Total time for operation

print('Time it takes to add 1 to each element in a list without NumPy:', total_time)
print('Time it takes to add 1 to each element in a list with NumPy:', total_time_with_np)

percent_faster = int((((total_time - total_time_with_np)/total_time)*100))
print('NumPy completes the operation', percent_faster, '% faster than a traditional list')

# Scalar Math
# np.add(arr,1)	Add 1 to each array element
# np.subtract(arr,2)	Subtract 2 from each array element
# np.multiply(arr,3)	Multiply each array element by 3
# np.divide(arr,4)	Divide each array element by 4 (returns np.nan for division by zero)
# np.power(arr,5)	Raise each array element to the 5th power

# Vector Math
# np.add(arr1,arr2)	Elementwise add arr2 to arr1
# np.subtract(arr1,arr2)	Elementwise subtract arr2 from arr1
# np.multiply(arr1,arr2)	Elementwise multiply arr1 by arr2
# np.divide(arr1,arr2)	Elementwise divide arr1 by arr2
# np.power(arr1,arr2)	Elementwise raise arr1 raised to the power of arr2
# np.array_equal(arr1,arr2)	Returns True if the arrays have the same elements and shape
# np.sqrt(arr)	Square root of each element in the array
# np.sin(arr)	Sine of each element in the array
# np.log(arr)	Natural log of each element in the array
# np.abs(arr)	Absolute value of each element in the array
# np.ceil(arr)	Rounds up to the nearest int
# np.floor(arr)	Rounds down to the nearest int
# np.round(arr)	Rounds to the nearest int


# Built-in Methods for Creating Arrays
# NumPy also has several built-in methods for creating arrays that are useful in practice. These methods are particularly useful:

# np.zeros(shape)
# np.ones(shape)
# np.full(shape, fill)

# One dimensional; 5 elements
print("-----------------------------------------")
print(np.zeros(5))
print("-----------------------------------------")
# Two dimensional; 2x2 matrix
print(np.zeros([2, 2]))
print("-----------------------------------------")
# 2 dimensional;  3x5 matrix
print(np.zeros([3, 5]))
print("-----------------------------------------")
# 3 dimensional; 3 4x5 matrices
print(np.zeros([3, 4, 5]))
print("-----------------------------------------")
# Similarly the np.ones() method returns an array of ones
print(np.ones(5))
print("-----------------------------------------")
print(np.ones([3, 4]))
print("-----------------------------------------")
# The np.full() method allows you to create an array of arbitrary values
# Create a 1d array with 5 elements, all of which are 3
print(np.full(5, 3))
print("-----------------------------------------")
# Create a 1d array with 5 elements, filling them with the values 0 to 4
print(np.full(5, range(5)))
print("-----------------------------------------")
# Sadly this trick won't work for multidimensional arrays
# NumPy also has useful built-in mathematical numbers
print(np.full([2, 5], np.pi))




