#Battle

def choose_chars(battle_char1, battle_char2):
    battle_char1 = int(input("What is the first character you would like to have battle?"))
    if battle_char1 in "Battle Simulator/characters.csv":
        print("Good choice!")
        battle_char2 = int(input("What is the second character you would like to have battle?"))
        def choose_chars2():
            if battle_char2 in "Battle Simulator/characters.csv":
                print("Good choice!")
                battle()
            elif battle_char2 not in "Battle Simulator/characters.csv":
                print("That isn't a character!")
                choose_chars2()
    elif battle_char1 not in "Battle Simulator/characters.csv":
        print("That isn't a character!")
        choose_chars()

def battle(battle_char1, battle_char2):
    if 