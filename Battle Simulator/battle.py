#Battle
from character_updater import *
import csv
import random

char_1_name = ""
char_2_name = ""
char_1 = ""
char_2 = ""


def choose_chars1(char_1_name, char_1):
    with open("Battle Simulator/characters.csv", "r") as file:
        char_1 = input("What is the first character you would like to have battle?")
        char_1_name = char_1
        if char_1 in "Battle Simulator/characters.csv":
            print("Good choice!")
            choose_chars2(char_2_name, char_2)
        elif char_1 not in "Battle Simulator/characters.csv":
            print("That isn't a character!")
            choose_chars1(char_1_name)

def choose_chars2(char_2_name, char_2):
    with open("Battle Simulator/characters.csv", "r") as file:
        char_2 = input("What is the second character you would like to have battle?")
        char_2_name = char_2
        if char_2 in "Battle Simulator/characters.csv":
            print("Good choice!")
            stats_and_speed(char_1_name, char_2_name, char_1, char_2)
        elif char_2 not in "Battle Simulator/characters.csv":
            print("That isn't a character!")
            choose_chars2(char_2_name)



def stats_and_speed(char_1_name, char_2_name, char_1, char_2):
    with open("Battle Simulator/characters.csv", "r") as file:
        char_1 = char_1_name
        char_2 = char_2_name
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if char_1 in row:
                char_1_stats = row
                char_1_health = char_1_stats["health"]
                char_1_strength = char_1_stats["strength"]
                char_1_defense = char_1_stats["defense"]
                char_1_speed = char_1_stats["speed"]
                char_1_level = char_1_stats["level"]

            if char_2 in row:
                char_2_stats = row
                char_2_health = char_2_stats["health"]
                char_2_strength = char_2_stats["strength"]
                char_2_defense = char_2_stats["defense"]
                char_2_speed = char_2_stats["speed"]
                char_2_level = char_2_stats["level"]

        if char_1_speed < char_2_speed:
            char_2_atk()
        elif char_2_speed > char_2_speed:
            char_1_atk()
        elif char_1_speed == char_2_speed:
            coin_flip = random.randint(1, 2)
            if coin_flip == 1:
                char_1_atk()
            elif coin_flip == 2:
                char_2_atk()
        return(char_1_stats, char_1_health, char_1_strength, char_1_defense, char_1_level, char_2_stats, char_2_health, char_2_strength, char_2_defense, char_2_level)

def char_1_atk(char_1_strength, char_2_health, char_2_defense):
    input("Enter anything to continue")
    damage = char_1_strength - char_2_defense
    damage_taken = char_2_health - damage
    char_2_health = char_2_health - damage_taken
    if char_2_health <= 0:
        char_1_win()
    elif char_2_health > 0:
        char_2_atk()

def char_2_atk(char_1_health, char_1_defense, char_2_strength):
    input("Enter anything to continue")
    damage = char_2_strength - char_1_defense
    damage_taken = char_1_health - damage
    char_1_health = char_1_health - damage_taken
    if char_1_health <= 0:
        char_2_win()
    elif char_1_health > 0:
        char_1_atk()

def char_1_win(char_1_name):
    print(char_1_name, "won!")
    char_1_level_up()
def char_2_win(char_2_name):
    print(char_2_name, "won!")
    char_2_level_up()





"""
import csv

with open("Notes/Class CSV sample - Sheet1.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        print(f"row {row[0]}, favorite color {row[1]}")
"""

"""
        "name": "",
        "health": 0,
        "strength": 0,
        "defense": 0,
        "speed": 0,
        "level": 0,
"""