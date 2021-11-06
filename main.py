# Author: Robert Murphy
# Date: 11/6/21
# Purpose:  assignment 7 regex

import sys
import getopt
import re
import os

#----------------------------------------------------------------------------------------------
#using regex to search output of os module
def regexSearch():

    #prints out any path in $PATH where it goes to C:\Users\Robert Murphy
    print("----------------------------------------------------------------------------")
    pattern1 = re.compile('Robert\sMurphy')
    length1 = len(pattern1.findall(str(os.environ)))
    print("Within the environment path variable, \"Robert Murphy\" is mentioned", length1, "times.")
    print(pattern1.findall(str(os.environ)))

    #will print out how many .py files there are in the directory

    pattern2 = re.compile("\.py")
    length = len(pattern2.findall(str(os.listdir())))
    x = os.getcwd()
    print("In", x, "there are", length, "python files:", pattern2.findall(str(os.listdir())))
    # print(pattern2.search(str(os.listdir())))
    print("The full contents of the directory are:")
    print(os.listdir())
    print()
    print("----------------------------------------------------------------------------")



#----------------------------------------------------------------------------------------------
argList = sys.argv[1:]
options = "r"
longOptions = ["regex"]
try:
    arguments, values = getopt.getopt(argList, options, longOptions)

    for currentArg, currentVal in arguments:
        if currentArg in ("-r", "--regex"):
            regexSearch()
except getopt.error as err:
    print("Wrong args. Enter -a or --asciiBump for asciiBump(). -m or --minMax for minMax().")
    print("-p or --pigLatin for pigLatin(). -b or --breakUp1 for breakup1(). -s or --breakUp2 for breakUp2()")


