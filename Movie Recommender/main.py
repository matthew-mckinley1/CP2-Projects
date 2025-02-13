#Matthew McKinley Movie Recommender

import csv

def filters():
    print("tomato")
    filter = int(input("What filter would you like to add to narrow down your search? \nPress 1 for Genre\nPress 2 for Directors\nPress 3 for Movie Length\nPress 4 for Actors\n:"))
    current_filters = []
    if filter == 1:
        current_filters.append()#genre
        pass #genre
    elif filter == 2:
        current_filters.append()#directors
        pass #directors
    elif filter == 3:
        current_filters.append()#length
        pass #length
    elif filter == 4:
        current_filters.append()#actors
        pass #actors
    else:
        print("You didn't input one of the numbers! Try again.")
        filters()

def print_all():
    pass #idk how to print, probably want it to look nice toooo

def recommend():
    pass

filters()