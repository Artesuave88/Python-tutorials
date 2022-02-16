# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 16:16:45 2022

@author: admin
"""
import random

def guess(x):
    random_num=random.randint(1,x)
    guess=0
    while guess!=random_num:
        guess=int(input(f"Guess a number between 1 and {x}\n"))
        if guess<random_num:
            print("sorry, too low")
        elif guess>random_num:
            print("Sorry, too high")
    print(f"Thats correct, the number is {random_num} ")
        

        
        
guess(100)

        