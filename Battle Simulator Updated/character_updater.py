#import csv so we can update the csv, and battle so we can use stuff from battle
import csv
from battle import *

# Validate that stats are within the range of 1-100
def check_stat(stat):
    #if it's not between 1 and 100, tell them to do it again
    while not (1 <= stat <= 100):
        print("Stat must be between 1 and 100.")
        stat = int(input(f"Please enter a valid value for {stat} (1-100): "))
    #when it IS between 1 and 100, then they can return
    return stat

#make it so that they can create their characters
def create_characters():
    #stats is a dictionary
    stats = {}
    #add the categories to the stats
    stats["name"] = input("What would you like to name your character?\n:")
    stats["health"] = check_stat(int(input("How much health would you like the character to have?\n:")))
    stats["strength"] = check_stat(int(input("How much strength would you like the character to have?\n:")))
    stats["defense"] = check_stat(int(input("How much defense would you like the character to have?\n:")))
    stats["speed"] = check_stat(int(input("How much speed would you like the character to have?\n:")))
    stats["level"] = 1
    #calls the function to save it to the csv
    save_to_csv(stats)

#saves it to the csv
def save_to_csv(stats):
    #opens the csv to append it
    with open("Battle Simulator Updated/characters.csv", "a", newline='') as file:
        #makes a csv writer and writes to the csv
        writer = csv.writer(file)
        writer.writerow([stats["name"], stats["health"], stats["strength"], stats["defense"], stats["speed"], stats["level"]])

#updates the csv
def update_character_csv(stats):
    characters = []
    #open the file and reads it
    with open("Battle Simulator Updated/characters.csv", "r") as file:
        csv_reader = csv.reader(file)
        #iterates through the file and adds the stats to the file
        for row in csv_reader:
            if row[0] == stats['name']:
                row = [stats['name'], stats['health'], stats['strength'], stats['defense'], stats['speed'], stats['level']]
                characters.append(row)

    with open("Battle Simulator Updated/characters.csv", "w", newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(characters)
#prints all of the characters stats
def check_stats():
    with open("Battle Simulator Updated/characters.csv", "r") as file:
        for row in file:
            print(row.strip())