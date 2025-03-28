#Matthew McKinley Coin Change Problem
import csv

def choose_country():
    country = int(input("Which country would you like to use?\n1) United States Dollar\n2)"))
    if country == 1:
        coin_change_US()
    elif country == 2:
        pass
    elif country == 3:
        pass
    elif country == 4:
        pass
    else:
        print("That isn't one of the options! TRY AGAIN...")
        choose_country()

def coin_change_US():
    with open("Coin Change Problem\currencies.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            for i in line:
                tom = "tomato"
                while tom == "tomato":
                    print("hehehehahaha")
    csv_reader = open("Coin Change Problem\currencies.csv", "r")
coin_change_US()