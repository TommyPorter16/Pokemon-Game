"""
Lab 10 part 4
Tommy Porter
November 26, 2022
"""

import random


class Pokemon:
    def __init__(self, name, attack, defense, max_health, current_health):
        self.name = name
        self.attack = int(attack)
        self.defense = int(defense)
        self.max_health = int(max_health)
        self.current_health = int(current_health)
        
    def __str__(self) -> str:
        """
        Return a string representation of the Pokemon.
        """
        pokemon = (self.name + " (health: " + str(self.current_health) + "/" + str(self.max_health) + ")")
        return pokemon
    
    def lose_health(self, amount: int) -> None:
        """
        Lose health from the Pokemon.
        """
        if amount < self.current_health and amount >= 0:
            self.current_health -= amount
        elif amount >= self.current_health:
            self.current_health = 0
            
    
    def is_alive(self) -> bool:
        """
        Return True if the Pokemon has health remaining.
        """
        if self.current_health > 0:
            return True
        else: 
            return False
    
    def revive(self):
        """
        Revive the Pokemon.
        """
        revive = random.random()
        if revive > 0.5:
            print(self.name + " has been revived!")
            self.current_health = self.max_health
            return True        
        
        
    def attempt_attack(self, other: "Pokemon") -> bool:
        """
        Attempt an attack on another Pokemon.
        This method can either return a bool, or return nothing
        (depends on your implementation)
        """
        luck = round(random.uniform(0.7,1.3),1)
        damage = round(float(self.attack) * luck)
        print(self.name + " is attacking " + other.name + " for " + str(damage) + " damage!")
        if damage > other.defense:
            other.lose_health(damage-other.defense)
            print("Attack hit! " + other.name + " has " + str(other.current_health) + " health remaining!")
        else:
            print("Attack missed!")
            
        
def read_pokemon_from_file(filename: str) -> list[Pokemon]:
    """
    Read a list of Pokemon from a file.
    """
    with open(filename,"r") as file:
        initial_data = file.readlines() 
    data = []
    for line in initial_data:
        line = line.replace("\n","")
        line = line.split("|")
        data.append(line)    
    return data
    
    
def main():
    """
    Battle of two Pokemon
    """
    list_of_pokemon = read_pokemon_from_file("all_pokemon.txt")
    pokemon1 = list_of_pokemon[random.randint(1,len(list_of_pokemon))]
    pokemon2 = pokemon1
    while pokemon2 == pokemon1:
        pokemon2 = list_of_pokemon[random.randint(1,len(list_of_pokemon))]
    pokemon1_name, pokemon1_attack, pokemon1_defense, pokemon1_health = pokemon1[0],pokemon1[1],pokemon1[2],pokemon1[2]
    pokemon2_name, pokemon2_attack, pokemon2_defense, pokemon2_health = pokemon2[0],pokemon2[1],pokemon2[2],pokemon2[2]
    pokemon1 = Pokemon(pokemon1_name, pokemon1_attack, pokemon1_defense, pokemon1_health, pokemon1_health)
    pokemon2 = Pokemon(pokemon2_name, pokemon2_attack, pokemon2_defense, pokemon2_health, pokemon2_health)
    print(f"Welcome, {pokemon1} and {pokemon2}!" + "\n")
    turn = 1
    play = True
    while play and turn <= 10:
        print("Round", turn, "begins:", pokemon1, pokemon2)
        pokemon1.attempt_attack(pokemon2)
        if not pokemon2.is_alive():
            print(pokemon2.name + " has fainted!")
            if not pokemon2.revive():
                print(pokemon1.name + " has won in " + str(turn) + " rounds!")
                play = False
                break
               
        pokemon2.attempt_attack(pokemon1)
        if not pokemon1.is_alive():
            print(pokemon1.name + " has fainted!")
            if not pokemon1.revive():
                print(pokemon2.name + " has won in " + str(turn) + " rounds!")
                play = False
        print("\n")
        turn += 1
    if turn == 11:
        print("It's a tie between", pokemon1, "and", pokemon2)
        
    
main()

