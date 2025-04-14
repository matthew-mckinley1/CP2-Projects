#Matthew McKinley Classes & Objects Notes

#What is a class in python?

    #A class is a blueprint for creating an object

#How do you create a python class?
class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nHealth: {self.hp}\nAttack Damage: {self.dmg}"

    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f"{self.name} attacked {opponent.name} for {self.dmg} and {opponent.name} now has {opponent.hp}.")
            if opponent.hp > 0:
                self.hp -= opponent.dmg
                print(f"{opponent.name} attacked {self.name} for {opponent.dmg} and {self.name} now has {self.hp}.")
                if self.hp <= 0:
                    print(f"{self.name} has been knocked out. {opponent.name} has won the battle!")
            else:
                print(f"{opponent.name} has been knocked out. {self.name} has won the battle!")

#How do you create a python object?

dracula = pokemon("Mr. Dracula", "Charizard", 10000,32)
salad = pokemon("Salad", "Bulbasaur", 32, 10000)

print(dracula)
#How to you call a method for an object?
dracula.battle(salad)
print(salad.hp)

#What is an object in python?

    #Every instance of a class is an object

#How do python classes relate to python objects?

#What are methods?

    #A function that is specific to a class

#Why do we use python classes?

    #It organizes your information better, it's convenient, simplifies later code
