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
        print("The string must have all letters. No numbers.")
        return 1


def str_mods(usr_choice):

    # asks user for a phrase and then takes the first letter of each word and changes it to +5 of its ascii codepoint
    user_word = input("Please enter a phrase: ")
    if check_string_input(user_word) == 0:
        print("------------------")

    if usr_choice == 1:
        new_str = list(user_word)

        for x in user_word:
            if x == 0:
                first = chr(ord(user_word[0]) + 5)
                new_str[0] = first
            else:
                if user_word[x] is " ":
                    second = ord(user_word[x + 1])
                    third = chr(second + 5)
                    new_str[x + 1] = third

        print("The new phrase is: ", new_str)

    # will take whatever punctuation is in the phrase and turns it into a ?
    if usr_choice == 2:
        second_str = list(user_word)
        punct_list = [".", "!", ",", ":", ";", "-", "_", "(", ")", "\"", "\'", "`"]

        for y in user_word:
            if user_word[y] in punct_list:
                second_str[y] = "?"

        print("The new phrase is: ", second_str)




if __name__ == '__main__':
    choice = input("Enter 1 to change the first letter of each word. \nEnter 2 to change all punctuation to ?")
    try:
        int_choice = int(choice)
    except:
        print("Please enter either 1 or 2")

    if (int_choice == 1 or int_choice == 2):
        str_mods(int_choice)
    else:
        print("Could not run str_mods")
else:
    print("sorry couldn't run main")

