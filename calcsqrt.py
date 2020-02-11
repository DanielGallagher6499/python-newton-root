#! /usr/bin/env python3

# Daniel Gallagher 
#Calculate the square root of a number.

def sqrt(x):

  # Check that x is positive.
  if x < 0:
    print("ERROR: Negative value inputted!")
    return -1
  else:
    print("Calculating please wait...")
    
  # initial guess for square root.
  z = x / 2.0

  #Continuously improve the guess.
  #Adapted from https://tour.golang.ord/flowcontrol/8
  while abs(x - (z*z)) > 0.000001:
    z = z - (((z * z) - x) / (2 * z))

  return z
myval = 63.0
print("The square root of ", myval , "is", sqrt(myval))


