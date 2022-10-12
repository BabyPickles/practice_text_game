# Error message from the incorrect choice
def error():
    print("Invalid response.")

# Player is dead
def dead():
    print("Better luck next time.")
    exit(0)

print("Welcome to the Practice Text game of 2022!")
print("Let's make your text based character.")
print(" ")

player_Fname = input("Enter your characters First Name: ")
player_Lname = input("Now enter your characters Last Name: ")
print("Nice to meet you", player_Fname, "", player_Lname)

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