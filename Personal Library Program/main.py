#Matthew McKinley Personal Library Program
#have the lists of books and titles for the list so i can update them with new stuff
books = []
titles = []

#Print simple and complicated list thingy
def printy():
    choose = int(input("Would you like a simple or a detailed list of the information (1 for simple, 2 for detailed)"))
    if choose == 1:
        for i in books:
            print(f"{i["Title"]} by {i["Author"]}")
    elif choose == 2:
        for i in books:
            print(f"{i["Title"]} by {i["Author"]} with {i["Pages"]} pages and it is a {i["Genre"]} book")
    else:
        print("You didn't put a 1 or a 2, try again.")
        printy()


#add the book function
def add_book(books, titles):
    title = input("What is the title of the book you want to add?\n")
    author = input("What is the author of that book?\n")
    pages = int(input("How many pages long is the book?\n"))
    genre = input("What genre is the book?\n")
    all = {
        "Title":title,
        "Author":author,
        "Pages":pages,
        "Genre":genre
    }
    titles.append(title)
    books.append(all)


def edit_book():
    #make new things to change the previous variables
    takeOut = str(input("What book would you like to edit?"))
    if takeOut in titles:
        indx = titles.index(takeOut)
        del books[indx]
        del books[titles]
        title = input("What is the new title of the book?\n")
        author = input("What is the new author of that book?\n")
        pages = int(input("How many pages long is the new book?\n"))
        genre = input("What genre is the new book?\n")
        all = {
            "Title":title,
            "Author":author,
            "Pages":pages,
            "Genre":genre
        }
        titles.append(title)
        books.append(all)
    elif takeOut not in titles:
        return("This is not in the list!")


#search function
def search_func(books, titles):
    search = str(input("What is the title of the book you want to check?"))
    if search in titles:
        print("This book is in the list\n\n")
    elif search not in books:
        print("This book is NOT in the list\n\n")
    else:
        print("This is not a book\n\n")

#remove a book function
def remove_func(books, titles):
    takeOut = str(input("What book would you like to remove?"))
    if takeOut in titles:
        indx = titles.index(takeOut)
        del books[indx]
    elif takeOut not in titles:
        return("This is not in the list!")
    
#main function to always run until they exit, having choices of what they want to do
def main(books, titles):
    while True:
        choice = int(input("\n\nPress 1 to print the list\nPress 2 to add to the list\nPress 3 to edit a book\nPress 4 to search through the list\nPress 5 to remove something from the list\nPress 6 to exit the program\n:"))
        if choice == 1:
            printy()
        elif choice == 2:
            add_book(books, titles)
        elif choice == 3:
            edit_book()
        elif choice == 4:
            search_func(books, titles)
        elif choice == 5:
            remove_func(books, titles)
        elif choice == 6:
            exit()
        else:
            print("You didn't put in a usable number!")
#running the main function to start the code
main(books, titles)