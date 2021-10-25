#Author: Robert Murphy
#assignment 5: branching

import sys
import platform
import statistics

print("Welcome to the information station!")
print()
print("The info station will let you learn more info about different things!")

newsession = input("Enter 1 for info about you system, 2 for information statistics, and 3 for string information: ")

try:
    int(newsession)
except:
    print("You did not enter a number")

session = int(newsession)

try:
    if session <= 3 and session >= 1:
        print("You will now be directed to ", session)
        print()
except:
    print("You did not enter 1, 2, or 3")

#1
if session == 1:
    print("The python version is", sys.version)
    print("The path variable is", sys.path)
    print("The processor being used is", platform.processor())
    print("The OS running is", platform.system())

#2
if session == 2:
    mylist= [1,2,3,4,5,6,7,8,9]
    print("Here is a list")
    print(mylist)
    print("The median is", statistics.median(mylist))
    print("The mean is", statistics.mean(mylist))
    print("standard deviation is", statistics.stdev(mylist))

#3
if session == 3:
    usr_str = input("Enter a string: ")
    print()
    if usr_str.isalnum() == True:
        print("Your string has all alphanumeric characters.")
    else:
        print("Your string is not all alphanumeric characters.")
    print()
    fin = usr_str.find("a")
    if fin != -1:
        print("Your string has an 'a' in it at index", fin)
    else:
        print("Your string does not have an 'a' in it.")
    print()
    cnt = usr_str.count("I")
    if cnt > 0:
        print("You said 'I'", cnt, "time(s) in your string.")
    else:
        print("You did not say 'I' in your string.")