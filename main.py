# Author: Robert Murphy
# Date: 10/31/21
# Purpose:  assignment 6

import sys, getopt

def asciiBump():
    word = input("Please enter a word: ")
    asci = 0
    mylist = []
    print(word, "is now ", end="")
    for x in word:
        asci = ord(x)
        asci += 1
        print(chr(asci), end="")
    print()
    print("Ascii value was raised by 1 for each letter")

def minMax():
    word2 = input("Please enter a word: ")
    num1 = min(word2)
    num2 = max(word2)
    print("The minimum ascii value for a character in the string is: ", num1, ord(num1))
    print("The maximum ascii value for a character in the string is: ", num2, ord(num2))


argList = sys.argv[1:]
options = "a:m"
longOptions = ["asciiBump", "minMax"]
try:
    arguments, values = getopt.getopt(argList, options, longOptions)

    for currentArg, currentVal in arguments:
        if currentArg in ("-a", "--asciiBump"):
            asciiBump()
        elif currentArg in ("-m", "--minMax"):
            minMax()
except getopt.error as err:
    print("Wrong args. Enter -a or --asciiBump for asciiBump() or -m or --minMax for minMax()")


