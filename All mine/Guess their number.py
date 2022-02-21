# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:27:13 2022

@author: admin
"""
import math
import random
guess=""
number=random.randint(0,10)
while guess!=number:

    guess=input("Guess a number: ")


# convert the num into string 
    guess = int(guess)
  




      
    if guess<number:
        print("Too low")
    if guess>number:
        print("Too high")
        

print("Yes, the number is ", number)
