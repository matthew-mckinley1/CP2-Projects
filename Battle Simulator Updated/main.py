#import everything from the other files
from character_updater import *
from battle import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from faker import Faker

# Initialize Faker for random character creation
fake = Faker()

#main function
def main():
    #infinite loop until they break
    while True:
        #take their choice
        choice = input("Press 1 to create a new character\nPress 2 to see a character's stats\nPress 3 to battle two characters\nPress 4 to view character stats visualization\nPress 5 to see basic stat analysis\nPress 6 to create a random character\nPress 7 to exit\n:")
        
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
        elif choice == "6":
            generate_random_character()
        elif choice == "7":
            break
        #if it's not one of those 6 numbers, then tell them to try again
        else:
            print("Invalid choice. Please try again.")

# Display character stat visualization (Radar Chart)
def display_character_visualization():
    char_name = input("Enter the character name for visualization: ")
    char_stats = load_character_stats(char_name)
    stats_data = pd.DataFrame({
    'Stat': ['health', 'strength', 'defense', 'speed'],
    'Value': [char_stats['health'], char_stats['strength'], char_stats['defense'], char_stats['speed']]
})
    # Check if character exists
    if char_stats is None:
        print("Character not found!")
        return
    else:
        titles = ['Health', 'Strength', 'Defense', 'Speed']
        values = [char_stats['health'], char_stats['strength'], char_stats['defense'], char_stats['speed']]
        plt.style.use('_mpl-gallery-nogrid')
        # make data
        x = values
        colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
        # plot
        fig, ax = plt.subplots()
        ax.pie(x, labels=titles, colors=colors, radius=3, center=(4, 4),
            wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 8), yticks=np.arange(1, 8))
        plt.show()


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