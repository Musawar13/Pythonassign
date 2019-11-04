# Q no 1. Write a Python program to print the following string in a specific format (see the output).

print('Twinkle, twinkle, little star')
print('      How I wonder what you are!')
print('           Up above the world so high')
print('           Like a diamond in the sky.')
print('Twinkle, twinkle, little star,.')
print('      How I wonder what you are!')

# Q 2. Write a Python program to get the Python version you are using

import sys

print (sys.version) 



# Q 3Write a Python program to display the current date and time.

import datetime

D_T = datetime.datetime.now()
print(D_T) 

# Q no 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

First_name = 'AHMED'
Last_name = 'ALI'
print (Last_name  +" "+ First_name)


#Q 6. Write a python program which takes two inputs from user and print them addition

A =  int(input("enter first no: "))
B =  int(input("enter second no: "))
sum= A+B
print("sum:",sum)

import math
from math  import pi
radius = float(input("enter a radius of circle:"))
print("for a circle with"+ str(radius) + "of radius")
A=(pi**2)
print ("the area is :" +str(A))





