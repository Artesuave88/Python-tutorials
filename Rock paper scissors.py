# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 18:26:04 2022

@author: admin
"""

import random
def play():
        user=input("Rock paper or scissors?\n'r' for rock, 'p' for paper, 's' for scissors\n")
        computer=random.choice(['r','p','s'])
        if user == computer:
            return f"Tie, The computer also chose {computer}"
        if is_winner(user,computer):
            return f"You won!, The computer chose {computer}"

        return f"You lost! The computer chose {computer}"



    
def is_winner(player,opponent):
    if(player=='r' and opponent =='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True 
    
print(play())