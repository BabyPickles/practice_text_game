## Practice Text game - Adventure game

from character import char_class, char_name
from scenes import introScene

def dead():
    print("You are dead. Better luck next time!")
    exit(0)

def error():
    print("Invalid response. Try something else.")

char_name(input("Please write your character name: "))

char_class()

introScene()


