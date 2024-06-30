import random

class Pokemon:
    def __init__(self, name, type, max_health,damage):
        self.name = name
        self.type = type
        self.max_health = max_health
        self.damage = damage
        self.current_health = max_health
        self.is_alive = True
    
    def attack(self, opponent):
        print("----------------------------------------------------------------------")
        print(f"{self.name} attacks {opponent.name} for {self.damage} damage!")
        opponent.take_damage(self.damage)
        print(f"{self.name} : {self.current_health} | {opponent.name} : {opponent.current_health}")
    
    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.current_health = 0
        self.check_alive()
    
    def check_alive(self):
        if self.current_health <= 0:
            self.is_alive = False
            print(f"{self.name} has fainted!")
        else:
            self.is_alive = True

class Fire(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Fire", 80,30)

class Water(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Water", 95,20)

class Grass(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Grass", 110,10)

class Game:
    def __init__(self):
        self.starter_pokemon = None
        self.opponent_pokemon = None
    
    def choose_starter(self):
        print("Choose your starter Pokemon:")
        print("1. Charmander (Fire)")
        print("2. Squirtle (Water)")
        print("3. Bulbasaur (Grass)")
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            self.starter_pokemon = Fire("Charmander")
        elif choice == "2":
            self.starter_pokemon = Water("Squirtle")
        elif choice == "3":
            self.starter_pokemon = Grass("Bulbasaur")
        else:
            print("Invalid choice, defaulting to Bulbasaur.")
            self.starter_pokemon = Grass("Bulbasaur")
        
        print(f"You chose {self.starter_pokemon.name}!")
    
    def generate_opponent(self):
        opponents = [Fire("Charmander"), Water("Squirtle"), Grass("Bulbasaur")]
        self.opponent_pokemon = random.choice(opponents)
        while self.opponent_pokemon.name == self.starter_pokemon.name:
            self.opponent_pokemon = random.choice(opponents)
        print(f"Your opponent is {self.opponent_pokemon.name}!")
    
    def battle(self, player_pokemon, opponent_pokemon):
        while player_pokemon.is_alive and opponent_pokemon.is_alive:
            player_pokemon.attack(opponent_pokemon)
            if opponent_pokemon.is_alive:
                opponent_pokemon.attack(player_pokemon)
    
    def check_winner(self, player_pokemon, opponent_pokemon):
        print("----------------------------------------------------------------------")
        if player_pokemon.is_alive:
            print(f"{player_pokemon.name} wins the battle!")
        else:
            print(f"{opponent_pokemon.name} wins the battle!")
        print("----------------------------------------------------------------------")
