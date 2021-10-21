#1 /usr/env/bin python3
""" Write a script that constructs the following pattern using a for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
BONUS- Come up with as many other methods to create this output as you can! """

def main():
    """ main function """
    loop=1
    char1 = "*" * loop
    print(char1)
    if loop == 1:
        increaseme(loop)
    elif loop == 5:
        decreaseme(loop)


def increaseme(loop):
    print("+", loop)
    loop = loop + 1
    char1 = "*" * 1
    print(char1)
    print("+", loop)

def decreaseme(loop):
    print("-")
    loop = loop - 1
    char1 = "*" * 1
    print(char1)

main()  
