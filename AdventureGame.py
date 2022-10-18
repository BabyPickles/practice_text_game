## Practice Text game - Adventure game

def dead():
    print("You are dead. Better luck next time!")
    exit(0)

def error():
    print("Invalid response. Try something else.")

from character import char_name, char_class
from Scenes import *

char_name(input("Please write your character name: "))

char_class()

introScene()


