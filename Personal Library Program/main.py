#Matthew McKinley Personal Library Program

books = []
titles = []

def addBook(books, titles):
    title = str(input("What is the title of the book you want to add?"))
    author = str(input("What is the author of that book?"))
    all = (title, author)
    titles.append(title)
    books.append(all)

def searchFunc(books):
    search = str(input("What is the title of the book you want to check?"))
    if search in books:
        print("This book is in the list")
    elif search not in books:
        print("This book is NOT in the list")
    else:
        print("This is not a book")

def removeFunc(books):
    takeOut = str(input("What book would you like to remove?"))
    if takeOut in books:
        books.remove(takeOut)
    elif takeOut not in books:
        return("This is not in the list!")
    

def main(books, titles):
    while True:
        choice = int(input("Press 1 to print the list\nPress 2 to add to the list\nPress 3 to search through the list\nPress 4 to remove something from the list\nPress 5 to exit the program\n:"))
        if choice == 1:
            print(books)
            print(titles)
        elif choice == 2:
            addBook(books, titles)
        elif choice == 3:
            searchFunc(books)
        elif choice == 4:
            removeFunc(books)
        elif choice == 5:
            exit()
        else:
            print("You didn't put in a usable number!")

main(books, titles)