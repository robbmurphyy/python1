# Author: Robert Murphy
# Date: 11/6/21
# Purpose:  assignment 7 regex

import sys, getopt, re, os

#----------------------------------------------------------------------------------------------
#using regex to search output of os module




#----------------------------------------------------------------------------------------------
argList = sys.argv[1:]
options = "r"
longOptions = ["asciiBump", "minMax", "pigLatin", "breakUp", "breakUp2"]
try:
    arguments, values = getopt.getopt(argList, options, longOptions)

    for currentArg, currentVal in arguments:
        if currentArg in ("-a", "--asciiBump"):
            asciiBump()
        elif currentArg in ("-m", "--minMax"):
            minMax()
        elif currentArg in ("-p", "--piglatin"):
            pigLatin()
        elif currentArg in ("-b", "--breakUp1"):
            breakUp1()
        elif currentArg in ("-s", "--BreakUp2"):
            breakUp2()
except getopt.error as err:
    print("Wrong args. Enter -a or --asciiBump for asciiBump(). -m or --minMax for minMax().")
    print("-p or --pigLatin for pigLatin(). -b or --breakUp1 for breakup1(). -s or --breakUp2 for breakUp2()")


