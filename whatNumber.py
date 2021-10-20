#!/usr/bin/env python3
""" if, elif, else - A simple program using conditionals to make a decision."""

import random


message = "You have 5 chances to guess the number in my head. It's between 1 and 7"

mynumber = random.randint(1, 7)
counter = 0
print(counter)
print(mynumber) # debug only

""" let's get started"""
def main():
    global counter
    print(str(counter)) #debug only
    print(message)
    counter = counter + 1 #increase by 1
    print("1." + str(counter))
    yourguess = input("What is your guess?\n>") # ADD validation that this is a valid entry
    # yourguess = 

    print("My number is: " + str(mynumber)) #debug only
    print("Your guess is: " + str(yourguess)) # add to previous attempt list and then use that list for next guess messages.
    # print Did you mean to guess that number again? if repeated value

    if yourguess == mynumber:
        print("You are Correct!")
        # break # why can't I have this here??????
    elif counter < 5:
        print("Try again")
        main()
    else:
        print("Game Over")

main()
