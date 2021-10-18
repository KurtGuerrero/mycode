"""An input asking the user's name.
An input asking what day of the week it is.
A print statement that reads:
Hello, <name>! Happy <day of the week>! """

def main():
    user_input1 = input("What is your name?\n>")
    user_input2 = input("What is the current Day Of The Week?").title()
"""    user_input2=user_input2.title()"""
    print("Hello, "+user_input1+"! Happy "+user_input2+"!")

main()

