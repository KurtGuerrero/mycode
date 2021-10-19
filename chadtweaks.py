#!/usr/bin/env python3
""" if, elif, else - A simple program using conditionals to make a decision."""

import random


message = "You have 5 chances to guess the number in my head. It's between 1 and 7"

mynumber = str(random.randint(1, 7))
print(mynumber)

""" let's get started"""
def main():
    counter = 0
    while True:
        counter = counter + 1 #increase by 1
        yourguess = input("What is your guess?\n>")
        print("My number is: " + str(mynumber))
        print("Your guess is: " + str(yourguess))

        if yourguess == mynumber:
            print("You are Correct!")
            break
        elif counter < 5:
            print("Try again")
        else:
            print("Game Over")
            break

main()
