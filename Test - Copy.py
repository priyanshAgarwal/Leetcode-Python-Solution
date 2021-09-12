# cook your dish here

# Python code to demonstrate copy operations

# importing "copy" for copy operations
from copy import copy

# initializing list 1
li1 = 5

# using copy to shallow copy
li2 = copy(li1)

# original elements of list

# adding and element to new list
li1 = 7

# checking if change is reflected
print ("The original elements after shallow copying")
print (li1)
print ("List2 after shallow copying")
print (li2)
