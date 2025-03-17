#Matthew McKinley Battle Simulator
from character_updater import *
from battle import *

def main():
    while True:
        match input("Press 1 to create a new character\nPress 2 to see a character's stats\nPress 3 to edit a character\nPress 4 to battle two characters\nPress 5 to exit\n:"):
            case "1":
                create_characters(stats, characters)
            case "2":
                check_stats()
            case "3":
                edit_characters(stats)
            case "4":
                choose_chars1(char_1_name, char_1)
            case "5":
                break
            case _:
                print("That isn't an applicable number!!")

main()