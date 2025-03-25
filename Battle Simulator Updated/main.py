#import everything from the other files
from character_updater import *
from battle import *
import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker

# Initialize Faker for random character creation
fake = Faker()

#main function
def main():
    #infinite loop until they break
    while True:
        #take their choice
        choice = input("Press 1 to create a new character\nPress 2 to see a character's stats\nPress 3 to battle two characters\nPress 4 to view character stats visualization\nPress 5 to see basic stat analysis\nPress 6 to exit\n:")
        
        #if and elifs for their options, run the functions necessary
        if choice == "1":
            create_characters()
        elif choice == "2":
            check_stats()
        elif choice == "3":
            choose_chars1()
        elif choice == "4":
            display_character_visualization()
        elif choice == "5":
            show_stat_analysis()
        #stop the infinite loop
        elif choice == "6":
            break
        #if it's not one of those 6 numbers, then tell them to try again
        else:
            print("Invalid choice. Please try again.")

# Display character stat visualization (Radar Chart)
def display_character_visualization():
    char_name = input("Enter the character name for visualization: ")
    char_stats = load_character_stats(char_name)
    if char_stats:
        labels = ['Health', 'Strength', 'Defense', 'Speed']
        values = [char_stats['health'], char_stats['strength'], char_stats['defense'], char_stats['speed']]
        
        # Radar chart plotting
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.set_theta_offset(3.14159 / 2)
        ax.set_theta_direction(-1)
        ax.set_rlabel_position(0)
        ax.set_xticks([n * 3.14159 / 2 for n in range(4)])
        ax.set_xticklabels(labels)
        ax.plot(values + values[:1], linewidth=2, linestyle='solid')
        ax.fill(values + values[:1], 'b', alpha=0.2)
        plt.title(f"Character: {char_name}'s Stats", size=15)
        plt.show()
    else:
        print("Character not found.")

# Show basic statistical analysis (Mean, Median, Max, Min)
def show_stat_analysis():
    df = pd.read_csv("Battle Simulator Updated/characters.csv", header=None, names=["name", "health", "strength", "defense", "speed", "level"])
    print("Statistical Analysis for Character Attributes:\n")
    
    # Calculate basic stats: mean, median, min, max
    for stat in ["health", "strength", "defense", "speed"]:
        stat_data = df[stat]
        print(f"{stat.capitalize()} - Mean: {stat_data.mean()}, Median: {stat_data.median()}, Min: {stat_data.min()}, Max: {stat_data.max()}")

#run the main function
main()