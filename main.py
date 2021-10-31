# Author: Robert Murphy
# Date: 10/31/21
# Purpose:  assignment 6

import sys, getopt

def asciiBump():
    word = input("Please enter a word: ")
    asci = 0
    print(word, "is now ", end="")
    for x in word:
        asci = ord(x)
        asci += 1
        print(chr(asci), end="")
    print()
    print("Ascii value was raised by 1 for each letter")
#----------------------------------------------------------------------------------------------------
def minMax():
    word2 = input("Please enter a word: ")
    num1 = min(word2)
    num2 = max(word2)
    print("The minimum ascii value for a character in the string is: ", num1, ord(num1))
    print("The maximum ascii value for a character in the string is: ", num2, ord(num2))
#----------------------------------------------------------------------------------------------------
def pigLatin():
    word3 = input("Please enter a sentence with no digits: ")
    for letter in word3:
        torf = letter.isdigit()
        if torf == True:
            print("You entered a sentence with digits, that's not allowed.")
            break

    list1 = word3.split(' ')
    consonants = ('b', 'B','c', 'C','d', 'D','f', 'F','g', 'G','h', 'H','j', 'J','k', 'K','l', 'L','m', 'M','n', 'N','p','P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'y' 'Y','v', 'V','x', 'X', 'z', 'Z')
    vowels = ["a", "A", "e", "E", "I", "i", "o", "O", "u", "U", "y "]
    translatedString =''

    for words in list1:
        firstlet = words[0]
        firstlet = str(firstlet)
        if firstlet in consonants:
            length = len(words)
            rem = words[1:length]
            translate = rem + firstlet + "ay"
            translatedString = translatedString + translate + " "
        elif firstlet in vowels:
            translate = words + "yay"
            translatedString = translatedString + translate + " "

    print(translatedString)

#-----------------------------------------------------------------------------------------------
def breakUp1():
    word4 = input("Please enter a sentence with no digits: ")
    for letter in word4:
        torf = letter.isdigit()
        if torf == True:
            print("You entered a sentence with digits, that's not allowed.")
            break
    punct = ["\'", "!", "?", ".", ",", "\"", ":", ";"]
    list3 = list(word4)
    for x in list3:
        if x.isspace():
            print()
        elif x.isalpha():
            print(x, end="")
        elif x in punct:
            print(x, end="")


#------------------------------------------------------------------------------------------------
def breakUp2():
    word5 = input("Please enter a sentence with no digits: ")
    for letter in word5:
        torf = letter.isdigit()
        if torf == True:
            print("You entered a sentence with digits, that's not allowed.")
            break
    list2 = word5.split(' ')
    for x in list2:
        print(x)

#----------------------------------------------------------------------------------------------
argList = sys.argv[1:]
options = "ampbsn:"
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


