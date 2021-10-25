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