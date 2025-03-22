import csv
from battle import *

# Validate that stats are within the range of 1-100
def check_stat(stat):
    while not (1 <= stat <= 100):
        print("Stat must be between 1 and 100.")
        stat = int(input(f"Please enter a valid value for {stat} (1-100): "))
    return stat

def create_characters():
    stats = {}
    stats["name"] = input("What would you like to name your character?\n:")
    stats["health"] = check_stat(int(input("How much health would you like the character to have?\n:")))
    stats["strength"] = check_stat(int(input("How much strength would you like the character to have?\n:")))
    stats["defense"] = check_stat(int(input("How much defense would you like the character to have?\n:")))
    stats["speed"] = check_stat(int(input("How much speed would you like the character to have?\n:")))
    stats["level"] = 1

    save_to_csv(stats)

def save_to_csv(stats):
    with open("Battle Simulator Updated/characters.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([stats["name"], stats["health"], stats["strength"], stats["defense"], stats["speed"], stats["level"]])

def update_character_csv(stats):
    characters = []
    with open("Battle Simulator Updated/characters.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == stats['name']:
                row = [stats['name'], stats['health'], stats['strength'], stats['defense'], stats['speed'], stats['level']]
            characters.append(row)

    with open("Battle Simulator Updated/characters.csv", "w", newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(characters)
