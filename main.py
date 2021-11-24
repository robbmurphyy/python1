# # Author: Robert Murphy
# # Date: 11/6/21
# # Purpose:  assignment 8 oop

class Bird:
    def __init__(self, title):
        self.name = title

    def color(self, color1, color2):
        self.color = color1
        self.second_color = color2

    def Wingspan(self, wingspan_cm):
        self.wingspan = wingspan_cm

    def BirdType(self, species):
        self.type = species

    def BirdSex(self, MorF):
        self.sex = MorF

def morfcheck(sex):
    y = False
    list = ['m', 'f']
    if sex in list:
        y = True
    return y

# def colorcheck(first, sec):
#     x = 0
#     colorlist = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "brown", "white", "black"]
#     for u in range(10):
#         if first.lower() is colorlist[u] and sec.lower() is colorlist[u]:
#                 print(u)
#                 x= 1
#                 print("Hi", x)
#                 break
#         else:
#             x= 0
#     if x == 1:
#         return True
#     else:
#         return False

if __name__ == '__main__':
    print("Please enter the characteristics for each bird!")
    print("Bird #1")
    name = input("Name: ")
    bird1 = Bird(name)

    print("You can only enter these colors. red, orange, yellow, green, blue, indigo, violet, brown, white, black")
    bird1.color(input("Primary color: "), input("Second color: "))
    bird1.Wingspan(int(input("Wing Span in cm: ")))
    bird1.BirdType(input("Type of Bird: "))
    bird1.BirdSex(input("Is it a male or female bird (M or F): "))
    print("Thanks")
    print("----------------------------")
    print("Bird #2")
    namee = input("Name: ")
    bird2 = Bird(namee)
    print()


    print("You can only enter these colors. red, orange, yellow, green, blue, indigo, violet, brown, white, black")
    bird2.color(input("Primary color: "), input("Second color: "))
    bird2.Wingspan(int(input("Wing Span in cm: ")))
    bird2.BirdType(input("Type of Bird: "))
    bird2.BirdSex(input("Is it a male or female bird (M or F): "))
    print("----------------------------------")
    print("Thanks. Here are your birds.")
    print("----------------------------------")
    print("Bird 1's attributes are: ")
    print(bird1.__dict__)
    print()
    print("Bird 2's attributes are")
    print(bird2.__dict__)

    deez = (dir(Bird))
    print()
    print("The methods each bird share are: ")
    for x in deez:
        if x[0] != '_':
            print(x)


print("-----------------------------------")