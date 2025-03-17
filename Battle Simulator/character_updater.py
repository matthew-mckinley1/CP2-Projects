#Character Updater

#imports everything from battle and csv
from battle import *
import csv

#list of characters
characters = []

#dictionary of stats
stats = {
        "name": "",
        "health": 0,
        "strength": 0,
        "defense": 0,
        "speed": 0,
        "level": 0,
    }

#take the character name
def get_name(stats, characters):
    stats["name"] = input("What would you like to name your character?\n:")
    characters.append(stats["name"])
#take the character health
def get_health(stats):
    while True:
        stats["health"] = int(input("How much health would you like the character to have?\n:"))
        if not stats["health"].isdigit():
            print("That's not a number! :(")
        else:
            if stats["health"] not in range(1, 100):
                print("That's not a number from 1-100! :(")
            else:
                print("That's a good number!")
                break
#take the character strength
def get_strength(stats):
    while True:
        stats["strength"] = int(input("How much strength would you like the character to have?\n:"))
        if not stats["strength"].isdigit():
            print("That's not a number! :(")
        else:
            if stats["strength"] not in range(1, 100):
                print("That's not a number from 1-100! :(")
            else:
                print("That's a good number!")
                break
#take the character defense
def get_defense(stats):
    while True:
        stats["defense"] = int(input("How much defense would you like the character to have?\n:"))
        if not stats["defense"].isdigit():
            print("That's not a number! :(")
        else:
            if stats["defense"] not in range(1, 100):
                print("That's not a number from 1-100! :(")
            else:
                print("That's a good number!")
                break
#take the character speed
def get_speed(stats):
    while True:
        stats["speed"] = int(input("How much speed would you like the character to have?\n:"))
        if not stats["speed"].isdigit():
            print("That's not a number! :(")
        else:
            if stats["speed"] not in range(1, 100):
                print("That's not a number from 1-100! :(")
            else:
                print("That's a good number!")
                break
#compile the stats
def create_characters(stats, characters):
    get_name(stats, characters)
    get_health(stats)
    get_strength(stats)
    get_defense(stats)
    get_speed(stats)
#make it so they can edit the character
def edit_characters(stats):
    edit = input("What character would you like to edit?") #ask what character they would like to input
    while True:
        if edit in "characters.csv": #check if it's in the file
            change = input("What statistic would you like to change?") #ask what stat they want to change
            if change in ["name", "health", "strength", "defense", "speed"]: #see if it's one of the stats
                if change == "name":
                    get_name(stats)
                elif change == "health":
                    get_health(stats)
                elif change == "strength":
                    get_strength(stats)
                elif change == "defense":
                    get_defense(stats)
                elif change == "speed":
                    get_speed(stats)
                else:
                    print("This is not going to show up!!!! teehee easter egg (get it cuz easter is soon i think :eyes:)") #silly thing that'll never show up!
            else:
                print("That isn't one of the statistics!")#if it's not in the list of stats
        else:
            print("That isn't a character!")#if its not in the file
#print the stats
def check_stats():
    with open("Battle Simulator/characters.csv", "r") as file:
        for row in file: #iterate through the 
            print(row)

def save_to_csv(stats, characters):
    with open("Battle Simulator/characters.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "health", "strength", "defense", "speed", "level"])
        for character in characters:
            writer.writerow([stats['name'], stats['health'], stats['strength'], stats['defense'], stats['speed'], stats['level']])

def level_up():
    def char_1_level_up(stats, characters, char_1):
        for character in characters:
            if character == char_1:
                stats["level"] = stats["level"] + 1
                with open("Battle Simulator/characters.csv", "a") as file:
                    writer = csv.writer(file)
                    writer.writerow(["name", "health", "strength", "defense", "speed", "level"])
                    for character in characters:
                        writer.writerow([stats['name'], stats['health'], stats['strength'], stats['defense'], stats['speed'], stats['level']])

    def char_2_level_up(stats, characters, char_2):
        for character in characters:
                if character == char_2:
                    stats["level"] = stats["level"] + 1
                    with open("Battle Simulator/characters.csv", "a") as file:
                        writer = csv.writer(file)
                        for character in characters:
                            writer.writerow([stats['name'] ,  stats['health'] ,  stats['strength'] ,  stats['defense'] ,  stats['speed'] ,  stats['level']])
    char_1_level_up()
    char_2_level_up()

def get_from_csv():
    with open("Battle Simulator/characters.csv", "r") as file:
        for row in file:
            print(row.strip())
        return
    
save_to_csv(stats, characters)


"""

character_writer = csv.writer(character_file)

        character_writer.writerow(['name','health','strength','defense','speed','bravery','class','level','wins'])

        for character in characters:
            
            character_writer.writerow([character['name'], character['health'], character['strength'], 
                                       character['defense'], character['speed'], character['bravery'], 
                                       character['class'], character['level'], character['wins']])

"""