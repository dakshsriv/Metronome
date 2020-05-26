#!/usr/bin/python3

# This program demonstrates function running from a variable in python

def make_pretty(func, func1):       # Defines make_pretty with the argument of func
    lst = [func, func1]
    def inner():                    # Defines inner without arguments
        print("I got decorated")    # Prints "I got decorated"
        for i in lst:
            i()                     # Calls the function that func was assigned to, i.e. make_pretty
    return inner                    # Calls and returns inner

def ordinary():                     # Defines ordinary without arguments
    print("I am ordinary")          # Prints "I am ordinary"

def cool():                         # Defines cool without arguments
    print("I am cool")              # Prints "I am cool"

pretty = make_pretty(ordinary, cool)# Calls make_pretty, telling that when the code func() is used, it runs the function ordinary
pretty()                            # Uses the variable pretty
