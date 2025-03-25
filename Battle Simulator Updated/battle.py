#import csv and random, and also everything from character_updater
import csv
import random
from character_updater import *

#lets them choose the characters
def choose_chars1():
    #takes the name for them to input to check character 1's stats
    char_1_name = input("What is the first character you would like to have battle?\n:")
    #loads the stats for character 1
    char_1_stats = load_character_stats(char_1_name)
    #if character 1 doesn't have stats, it doesn't exist
    if not char_1_stats:
        print("That character doesn't exist!")
        #runs it again to make them retry
        choose_chars1()
    else:
        print(f"Good choice! {char_1_name} selected.")
        #runs choose 2 to choose another character
        choose_chars2(char_1_name, char_1_stats)

#choose character two
def choose_chars2(char_1_name, char_1_stats):
    #takes the name for them to input to check character 2's stats
    char_2_name = input("What is the second character you would like to have battle?\n:")
    #loads the stats for character 2
    char_2_stats = load_character_stats(char_2_name)
    #if character 2 doesn't have stats, it doesn't exist
    if not char_2_stats:
        print("That character doesn't exist!")
        #runs it again to make them retry
        choose_chars2(char_1_name, char_1_stats)
    else:
        print(f"Good choice! {char_2_name} selected.")
        #runs stats and speed to get the start of the battle
        stats_and_speed(char_1_name, char_2_name, char_1_stats, char_2_stats)

# Function to load character stats from csv
def load_character_stats(character_name):
    #opens the file in read mode
    with open("Battle Simulator Updated/characters.csv", "r") as file:
        #makes a reader and returns the dictionary
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == character_name:
                return {
                    'name': row[0],
                    'health': int(row[1]),
                    'strength': int(row[2]),
                    'defense': int(row[3]),
                    'speed': int(row[4]),
                    'level': int(row[5])
                }
    return None

# Stats and speed comparison to determine who attacks first
def stats_and_speed(char_1_name, char_2_name, char_1_stats, char_2_stats):
    #makes temporary health variables to check
    temp_health_1 = char_1_stats['health']
    temp_health_2 = char_2_stats['health']
    #speed comparison to see who goes first
    if char_1_stats['speed'] > char_2_stats['speed']:
        char_1_atk(char_1_stats, char_2_stats, temp_health_1, temp_health_2)
    elif char_1_stats['speed'] < char_2_stats['speed']:
        char_2_atk(char_1_stats, char_2_stats, temp_health_1, temp_health_2)
    else:
        # Coin flip for speed tie
        coin_flip = random.randint(1, 2)
        if coin_flip == 1:
            char_1_atk(char_1_stats, char_2_stats, temp_health_1, temp_health_2)
        else:
            char_2_atk(char_1_stats, char_2_stats, temp_health_1, temp_health_2)

# Character 1 attack
def char_1_atk(char_1_stats, char_2_stats, temp_health_1, temp_health_2):
    #makes them press enter to do the next attack
    input("Press Enter to attack...")
    damage = char_1_stats['strength'] - char_2_stats['defense']
    temp_health_2 -= max(damage, 0)  # Prevent negative damage
    #prints the outcome of that attack
    print(f"{char_1_stats['name']} attacks! {char_2_stats['name']} now has {temp_health_2} HP.")
    #checks if the enemy has less than or 0 health
    if temp_health_2 <= 0:
        char_1_win(char_1_stats['name'])
        #if they're not dead, character 2 attacks
    else:
        char_2_atk(char_1_stats, char_2_stats, temp_health_1, temp_health_2)

# Character 2 attack
def char_2_atk(char_1_stats, char_2_stats, temp_health_1, temp_health_2):
    #makes them press enter to do the next attack
    input("Press Enter to attack...")
    damage = char_2_stats['strength'] - char_1_stats['defense']
    temp_health_1 -= max(damage, 0)  # Prevent negative damage
    #prints the outcome of that attack
    print(f"{char_2_stats['name']} attacks! {char_1_stats['name']} now has {temp_health_1} HP.")
    #checks if the enemy has less than or 0 health
    if temp_health_1 <= 0:
        char_2_win(char_2_stats['name'])
        #if they're not dead, character 1 attacks
    else:
        char_1_atk(char_1_stats, char_2_stats, temp_health_1, temp_health_2)

# Character 1 wins
def char_1_win(char_1_name):
    print(f"{char_1_name} won!")
    #level up
    level_up(char_1_name)

# Character 2 wins
def char_2_win(char_2_name):
    print(f"{char_2_name} won!")
    #level up
    level_up(char_2_name)

# Level up function (generalized)
def level_up(character_name):
    #takes that character's name, adds a level
    stats = load_character_stats(character_name)
    stats['level'] += 1
    #updates the leveled up stat
    update_character_csv(stats)
    #tells the user that they leveled up
    print(f"{character_name} leveled up! New level: {stats['level']}")

#updates the character's stats with the new level
def update_character_csv(stats):
    characters = []
    #opens the file in read mode
    with open("Battle Simulator Updated/characters.csv", "r") as file:
        #makes the reader and saves the current stats
        csv_reader = csv.reader(file)
        #iterates through the list
        for row in csv_reader:
            if row[0] == stats['name']:
                row = [stats['name'], stats['health'], stats['strength'], stats['defense'], stats['speed'], stats['level']]
                characters.append(row)
    #opens the file as write and edits the file with the new levels
    with open("Battle Simulator Updated/characters.csv", "w", newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(characters)