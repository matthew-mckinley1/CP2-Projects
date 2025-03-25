#import csv so we can update the csv, and battle so we can use stuff from battle
import csv
from battle import *
import random
from faker import Faker

# Initialize Faker for random character creation
fake = Faker()

# Validate that stats are within the range of 1-100
def check_stat(stat):
    #if it's not between 1 and 100, tell them to do it again
    while not (1 <= stat <= 100):
        print("Stat must be between 1 and 100.")
        stat = int(input(f"Please enter a valid value for {stat} (1-100): "))
    #when it IS between 1 and 100, then they can return
    return stat

# Generate random character details
def generate_random_character():
    # Generating random name and backstory using Faker
    name = fake.name()
    backstory = fake.text(max_nb_chars=100)
    health = random.randint(50, 100)
    strength = random.randint(10, 50)
    defense = random.randint(5, 30)
    speed = random.randint(20, 40)
    return {"name": name, "backstory": backstory, "health": health, "strength": strength, "defense": defense, "speed": speed, "level": 1}

#make it so that they can create their characters
def create_characters():
    #stats is a dictionary
    stats = {}
    
    # Option to create random or custom character
    choice = input("Press 1 for a custom character or 2 for a random character: ")
    if choice == "1":
        stats["name"] = input("What would you like to name your character?\n:")
        stats["health"] = check_stat(int(input("How much health would you like the character to have?\n:")))
        stats["strength"] = check_stat(int(input("How much strength would you like the character to have?\n:")))
        stats["defense"] = check_stat(int(input("How much defense would you like the character to have?\n:")))
        stats["speed"] = check_stat(int(input("How much speed would you like the character to have?\n:")))
        stats["level"] = 1
    elif choice == "2":
        stats = generate_random_character()
        print(f"Random character generated: {stats['name']}")
    
    save_to_csv(stats)

#saves it to the csv
def save_to_csv(stats):
    #opens the csv to append it
    with open("Battle Simulator Updated/characters.csv", "a", newline='') as file:
        #makes a csv writer and writes to the csv
        writer = csv.writer(file)
        writer.writerow([stats["name"], stats["health"], stats["strength"], stats["defense"], stats["speed"], stats["level"]])

#prints all of the characters stats
def check_stats():
    with open("Battle Simulator Updated/characters.csv", "r") as file:
        for row in file:
            print(row.strip())