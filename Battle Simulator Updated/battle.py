import csv
import random
from character_updater import *

def choose_chars1():
    char_1_name = input("What is the first character you would like to have battle?\n:")
    char_1_stats = load_character_stats(char_1_name)
    if not char_1_stats:
        print("That character doesn't exist!")
        choose_chars1()
    else:
        print(f"Good choice! {char_1_name} selected.")
        choose_chars2(char_1_name, char_1_stats)

def choose_chars2(char_1_name, char_1_stats):
    char_2_name = input("What is the second character you would like to have battle?\n:")
    char_2_stats = load_character_stats(char_2_name)
    if not char_2_stats:
        print("That character doesn't exist!")
        choose_chars2(char_1_name, char_1_stats)
    else:
        print(f"Good choice! {char_2_name} selected.")
        stats_and_speed(char_1_name, char_2_name, char_1_stats, char_2_stats)

# Function to load character stats from CSV
def load_character_stats(character_name):
    with open("Battle Simulator Updated/characters.csv", "r") as file:
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
    temp_health_1 = char_1_stats['health']
    temp_health_2 = char_2_stats['health']

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

# Character 1 attacks
def char_1_atk(char_1_stats, char_2_stats, temp_health_1, temp_health_2):
    input("Press Enter to attack...")
    damage = char_1_stats['strength'] - char_2_stats['defense']
    temp_health_2 -= max(damage, 0)  # Prevent negative damage
    print(f"{char_1_stats['name']} attacks! {char_2_stats['name']} now has {temp_health_2} HP.")
    
    if temp_health_2 <= 0:
        char_1_win(char_1_stats['name'])
    else:
        char_2_atk(char_1_stats, char_2_stats, temp_health_1, temp_health_2)

# Character 2 attacks
def char_2_atk(char_1_stats, char_2_stats, temp_health_1, temp_health_2):
    input("Press Enter to attack...")
    damage = char_2_stats['strength'] - char_1_stats['defense']
    temp_health_1 -= max(damage, 0)  # Prevent negative damage
    print(f"{char_2_stats['name']} attacks! {char_1_stats['name']} now has {temp_health_1} HP.")
    
    if temp_health_1 <= 0:
        char_2_win(char_2_stats['name'])
    else:
        char_1_atk(char_1_stats, char_2_stats, temp_health_1, temp_health_2)

# Character 1 wins
def char_1_win(char_1_name):
    print(f"{char_1_name} won!")
    level_up(char_1_name)

# Character 2 wins
def char_2_win(char_2_name):
    print(f"{char_2_name} won!")
    level_up(char_2_name)

# Level up function (generalized)
def level_up(character_name):
    stats = load_character_stats(character_name)
    stats['level'] += 1
    update_character_csv(stats)
    print(f"{character_name} leveled up! New level: {stats['level']}")

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