# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 16:16:45 2022

@author: admin
"""
import random

def comp_guess(x):
    low=1
    high=x
    feedback=""
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} too high (H), low(L), or correct(C)?\n").lower()
        if feedback=='h':
            high = guess-1
        elif feedback=='l':
            low = guess+1
            
    print(f"I got your number correct. It's {guess}")
            
        
        
comp_guess(100)

        