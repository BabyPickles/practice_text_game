# Error message from the incorrect choice
def error():
    print("Invalid response.")

# Player is dead
def dead():
    print("Better luck next time.")
    exit(0)

# Character name requirements

def char_name(name):
    if len(name) < 3:
        print("Invalid input. Character name needs to be 3 or more characters.")


print("Welcome to the Practice Text game of 2022!")
print("Let's make your text based character.")
print(" ")

def create_character():
    char_name(input("Enter your characters name: "))
        if char_name = True:
            start()
        elif char_name = False:
            create_character()

print("Nice to meet you " + str(char_name_req))

def start():
    print("Welcome to the text based Adventure game! This is an early Alpha ;)")
    setting = input("Would you like to travel to the Desert or Jungle?")
    if setting == 'Desert':
        print("Welcome to the desert!")
    response = input("You are thirsty and it's super hot. Do you carry on into the desert or wait?")
    if response == 'carry on':
        print(" ")
        print("Moves on")
    elif response == 'wait':
        print(" ")
        print("Dead")
        dead()
    else:
        error()


start()