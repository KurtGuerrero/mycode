#!/usr/bin/env python3

def main():
    icecream= ["flavors", "salty"]
    northerntrust= ["Alex","Andrew","Dave","Julia","Kurt","Marlon","Roger","Seth","Tim","Viq"]
    # Append the integer (not string!) 99 to the list icecream.
    int_to_append= 99
    icecream.append(int_to_append)
    # print(icecream)
    # Include an input asking for a number between 0 and 9. Use this number to identify one of the students from the northerntrust list!
    num=int(input("Pick a number between 0-9\n>"))
    # Using the appended list and the input, make this output (emphasis placed):
    # <99> <flavors>, and <student name> chooses to be <salty>.
    print(f"{icecream[2]} {icecream[0]} and {northerntrust[num]} chooses to be {icecream[1]}.")
 
main()
