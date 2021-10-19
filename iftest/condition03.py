#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")

# Code Customization 01 - If hostname was found to be mtg, print a second line that says hostname matches expected config to the screen.
if hostname.lower() == "mtg":
    print("hostname matches expected config")

# Code Customization 02 - Before the program ends, always display to the user Exiting the script.
print("Exiting the script")
