#Matthew McKinley Coin Change Problem
import  csv

def choose_country():
    country = int(input("Which country would you like to use?\n1) United States Dollar\n2)"))
    if country == 1:
        coin_change_US()
    elif country == 2:
        
    elif country == 3:

    elif country == 4:
        
    else:
        print("That isn't one of the options! TRY AGAIN...")
        choose_country()

def coin_change_US():
    with open("Coin Change Problem\currencies.csv", "r") as file:
        for row in file:
            row[0] = 