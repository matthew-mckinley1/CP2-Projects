#import everything from the other files
from character_updater import *
from battle import *

#main function
def main():
    #infinite loop until they break
    while True:
        #take their choice
        choice = input("Press 1 to create a new character\nPress 2 to see a character's stats\nPress 3 to battle two characters\nPress 4 to exit\n:")
        #if and elifs for their options, run the functions necessary
        if choice == "1":
            create_characters()
        elif choice == "2":
            check_stats()
        elif choice == "3":
            choose_chars1()
        #stop the infinite loop
        elif choice == "4":
            break
        #if it's not one of those 4 numbers, then tell them to try again
        else:
            print("Invalid choice. Please try again.")
#run the main function
main()