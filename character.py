# This is where we define the character.

# Character name
def char_name(name):
    if len(name) <= 3:
        print("\nInvalid character name. Needs to be 3 or more characters")
    elif len(name) >= 25:
        print("\nInvalid character name. Cannot be more then 25 characters.")
    else:
        print("\nWelcome " + "\033[1m" + name + "\033[0m" + " to the world of Vadania.")

# Character Class
def char_class():
    classes = ["Warrior", "Hunter", "Mage"]
    print("Please select the class of your character: ")
    userInput = ""
    while userInput not in classes:
        print("Options: Warrior, Hunter, Mage")
        userInput = input()
        if userInput == "Warrior":
            char_class = Warrior
            print("Very well, a " + char_class + " it is.")
        elif userInput == "Hunter":
            char_class = Hunter
            print("Very well, a " + char_class + " it is.")
        elif userInput == "Mage":
            char_class = Mage
            print("Very well, a " + char_class + " it is.")
        else:
            print("\nInvalid class, please choose one of the options.")

# Character Gender
#def char_gender():

# Character Class
#def char_class():