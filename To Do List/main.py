#Matthew McKinley To Do List

#Create a program that allows the user to view, add, delete, and mark tasks on a to do list that is saved on a seperate text file.
#Create a to do list (Kept on a txt file)
#Add items to the to do list
#Mark item as complete
#Delete item from to do list

def view_items():
    with open("To Do List\to_do_list.txt", "r") as file:
        for row in "To Do List\to_do_list.txt": #I don't know if this is how to do this
            print(row)
        
        main()



def add_items():
    with open("To Do List\to_do_list.txt", "a") as file:
        add = input("What would you like to add to the to do list?")
        #"To Do List\to_do_list.txt".append(add) this is not how it works
        main()


def mark_items():
    with open("To Do List\to_do_list.txt", "w+") as file:
        mark = input("What would you like to mark as done in the to do list")
        #add something to show that they're marked
        main()


def delete_items():
    with open("To Do List\to_do_list.txt", "w") as file:
        delete = input("What would you like to delete from the to do list?")
        #remove stuff
        main()


def main():
    while True:
        choice = input("Welcome to the To Do List!\nPress 1 to View To Do List\nPress 2 to Add Items\nPress 3 to Mark Items as Done\nPress 4 to Delete Items\nPress 5 to Leave\n:")
        if choice == 1:
            view_items()
        elif choice == 2:
            add_items()
        elif choice == 3:
            mark_items()
        elif choice == 4:
            delete_items()
        elif choice == 5:
            break

main()