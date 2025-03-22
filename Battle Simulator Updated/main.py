from character_updater import *
from battle import *

def main():
    while True:
        choice = input("Press 1 to create a new character\nPress 2 to see a character's stats\nPress 3 to battle two characters\nPress 4 to exit\n:")
        if choice == "1":
            create_characters()
        elif choice == "2":
            check_stats()
        elif choice == "3":
            choose_chars1()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def check_stats():
    with open("Battle Simulator Updated/characters.csv", "r") as file:
        for row in file:
            print(row.strip())

main()