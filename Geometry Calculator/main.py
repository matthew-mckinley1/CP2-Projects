#import all of the chicken nuggets from the other files
from shape_management import *
from sorting import *

#make lists to hold the information
rects = []
tris = []
circs = []

#main function
def main():
    print("Hello! This is a 2D geometry calculator!")
    #keep it running forever
    while True:
        #main ui
        print("\nMain Menu:")
        print("1. Input a New Shape")
        print("2. Compare/Sort Existing Shapes")
        print("3. Exit")
        #take their choice
        choice = input("Choose an option: ").strip()
        #if the choice is 1, make them input a rectangle, triangle, or a circle
        if choice == '1':
            print("\nWhich shape would you like to enter?")
            print("1. Rectangle")
            print("2. Triangle")
            print("3. Circle")
            shape_choice = input("Enter your choice: ").strip()
            #makes that shape
            if shape_choice == '1':
                rects.append(make_rect())
            elif shape_choice == '2':
                tris.append(make_tri())
            elif shape_choice == '3':
                circs.append(make_circle())
            else:
                print("Invalid choice.")
        elif choice == '2':
            sort_main(rects, tris, circs)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")
#calls main function
main()