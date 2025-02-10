#Matthew McKinley Personal Library Program
#have the lists of books and titles for the list so i can update them with new stuff
books = []
titles = []



#add the book function
def add_book(books, titles):
    title = str(input("What is the title of the book you want to add?\n"))
    author = str(input("What is the author of that book?\n"))
    all = (title, author)
    titles.append(title)
    books.append(all)

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
        choice = int(input("\n\nPress 1 to print the list\nPress 2 to add to the list\nPress 3 to search through the list\nPress 4 to remove something from the list\nPress 5 to exit the program\n:"))
        if choice == 1:
            print(books)
        elif choice == 2:
            add_book(books, titles)
        elif choice == 3:
            search_func(books, titles)
        elif choice == 4:
            remove_func(books, titles)
        elif choice == 5:
            exit()
        else:
            print("You didn't put in a usable number!")
#running the main function to start the code
main(books, titles)