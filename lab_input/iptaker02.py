#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""


def part2():
    user_input2 = input("Please enter the Vendor name of your device:")
    print("1.You responded with: ", user_input2)
    print("2.You responded with " + user_input2)

def main():

    # collect string input from the user
    user_input = input("Please enter an IPv4 IP address:")
    part2()
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)

main()




