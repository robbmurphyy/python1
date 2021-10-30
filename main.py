# Author: Robert Murphy
# Date: 10/31/21
# Purpose:  assignment 6



#checks to see if the input has all letters or - in it
def check_string_input(input):
    word2 = input
    hyphen = "-"
    try:
        TorF = word2.isalpha()
    except:
        print("You did not enter a string")
    if TorF == True:
        return 0
    if TorF == False and hyphen in word2:
        return 0
    if TorF == False:
        print("The string must have all letters. No numbers, symbols, or spaces.")
        return 1


def pigLatin():

    # asks user for a word, counts num of letters, and then prints
    user_word = input("Please enter a word: ")
    if check_string_input(user_word) == 0:
        print("------------------")




if __name__ == '__main__':
    pigLatin()
else:
    print("sorry couldn't run main")

