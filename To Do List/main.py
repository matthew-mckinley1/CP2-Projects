#Matthew McKinley To Do List

#Create a program that allows the user to view, add, delete, and mark tasks on a to do list that is saved on a seperate text file.
#Create a to do list (Kept on a txt file)
#Add items to the to do list
#Mark item as complete
#Delete item from to do list

#List of items to keep in a list to save
good_items = []

#view items function
def view_items():
    #opens and closes the text file and reads it
    with open("To Do List/to_do_list.txt", "r") as file:
        for row in file:
            print(row.strip())  #strip to avoid newline characters
        return

#add items to the list function
def add_items():
    #opens and closes the text file and appends to it
    with open("To Do List/to_do_list.txt", "a") as file:
        #take the input of what they want
        add = input("What item would you like to add? ")
        file.write(add + "\n")  #add a newline character after each item
        #adds to the good items list
        good_items.append(add)
        return

#mark items as complete function
def mark_items():
    #opens the file and reads iut
    with open("To Do List/to_do_list.txt", "r") as file:
        lines = file.readlines()
    #takes the input on what they want to mark as done
    mark = input("What item would you like to mark as done? ")
    item_found = False
    #opens it again with it in write mode
    with open("To Do List/to_do_list.txt", "w") as file:
        #iterates through each of the lines and checking if the one that they want is in it, and then marking that
        for line in lines:
            if line.strip() == mark:
                item_found = True
                file.write(mark + " ***\n")  #add '***' to mark as done
            else:
                file.write(line)  # Keep the other lines unchanged
    if not item_found:
        print("That item is not in the list!")
        return

#function to delete items
def delete_items():
    delete = input("What item would you like to delete? ")
    #checks if it is in the items
    if delete in good_items:
        good_items.remove(delete)
        #opens the file and writes it
        with open("To Do List/to_do_list.txt", "w") as file:
            for item in good_items:
                file.write(item + "\n")  # Write each item back to the file
        print(f"Item '{delete}' deleted.")
    else:
        print("That item is not in the list!")

#main function to do UI
def main():
    #make it so that it can end
    running = True
    while running == True:
        #main UI
        choice = input("Welcome to the To Do List!\nPress 1 to View List\nPress 2 to Add Items\nPress 3 to Mark Items\nPress 4 to Delete Items\nPress 5 to Leave\n: ")
        if choice == '1':
            view_items()
        elif choice == '2':
            add_items()
        elif choice == '3':
            mark_items()
        elif choice == '4':
            delete_items()
        elif choice == '5':
            running = False

#call it so it runs
main()