#Matthew McKinley Battle Simulator
from character_updater import *
from battle import *

def main():
    while True:
        match input("Press 1 to create a new character\nPress 2 to see a character's stats\nPress 3 to edit a character\nPress 4 to battle two characters\nPress 5 to exit\n:"):
            case "1":
                new_char()
            case "2":
                print_char()
            case "3":
                edit_char
            case "4":
                battle()
            case "5":
                break
            case _:
                print("That isn't an applicable number!!")

main()