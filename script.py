#Modules import
from random import randint

#Defining functions used throughout the program

def select_pokemons():
    pokemons = ['Pikachu', 'Renekton', 'Maokai']
    pokemon_1 = input('\nPlayer 1, please select a pokemon ')
    pokemon_2 = input('\nPlayer 2, please select a pokemon ')
    while not(pokemon_1 in pokemons and pokemon_2 in pokemons):
        print('\nInvalid pokemon selection')
        pokemon_1 = input('\nPlayer 1, please select a pokemon ')
        pokemon_2 = input('\nPlayer 2, please select a pokemon ')

def print_instructions():
    print(info.instructions)

def print_pokemons():
    print('\n' + info.pikachu)
    print('\n' + info.renekton)
    print('\n' + info.maokai)


#Info class definition
class Info:
    instructions = '''
    Welcome to Pokemon game!
    In this game, you and your opponent will choose a Pokemon our of 4 available Pokemons.
    The game objective is to defeat the opponents Pokemon. 
    The first part of each turn is called the upkeep. Here the pokemons regain their health, mana and gain gold.
    Each Pokemon gets 5 gold in the upkeep, health and mana regen are specific to each pokemon.
    In the second part, the player can choose only one of the following actions:

    1: Rest
        The Pokemon rests and regains 10 health.

    2: Shop
        The Pokemon visits the shop where items that increase the Pokemons attributes can be bought. 

    3: Attack
        The Pokemon attacks the other Pokemon. Damage dealt is calculated as Attack damage - armor.

    4: Jungle
        The Pokemon visits the jungle where one of the following scenarios randomly occurs: 
            1. Rumble ambush: -10 health, -10 gold
            2. Gold sack:     +15 gold
            3. Lake:          +20 health
            4. Meditation:    +1 Health regen, +2 armor
        As you can see, it is beneficial to visit the jungle. 

    5: Cast a special ability
        This is specific to every Pokemon, there is one Pokemon that has no ability!
    '''

    pikachu  = '''
    Pikachu:
    Light caster, excels from start, has very high burst potential!
    health        = 140
    health_regen  = 8
    armor         = 5
    attack_damage = 15
    mana          = 100
    mana_regen    = 20

    fireball: Costs 60 mana and deals 40 damage to target Pokemon
    '''
    
    renekton = '''
    Renekton:
    Tough figher, has no abilities, uses brute force to win!
    health        = 150
    health_regen  = 12
    armor         = 10
    attack_damage = 20
     '''
    
    maokai = '''
    Maokai:
    Massive creature, that grows overtime until it can not be stopped!
    health        = 170
    health_regen  = 10
    armor         = 50
    attack_damage = 10
    mana          = 120
    mana_regen    = 10
 
    overgrow: Costs 20 mana and Maokai permanently gains 5 health, 1.5 health_regen, 0.5 armor and 0.4 attack_damage
    '''

#Store class definition
class Store:
    '''Contains items that can be bought by pokemons'''
    item           = ['Shield', 'Sword', 'Stone of life', 'Philosophers stone', 'Vest', 'Great sword', 'Book of magic']
    description    = ['+10 armor', '+11 Attack damade', '+8 Health regen', '+5 Mana regen', '+30 armor', '+25 Attack damage', '+10 Mana regen']
    cost            = [30, 30, 30, 30, 100, 100, 90]
    health          = [0, 0, 0, 0, 0, 0, 0]
    health_regen    = [0, 0, 8, 0, 0, 0, 0]
    armor           = [10, 0, 0, 0, 30, 0, 0] 
    attack_damage   = [0, 11, 0, 0, 0, 25, 0]
    mana            = [0, 0, 0, 0, 0, 0, 0]
    mana_regen      = [0, 0, 0, 5, 0, 0, 10]

#Pokemon parent class definition
class Pokemon:
    '''Basic Pokemon class, includes all of the basic pokemon functions but no abilities'''
    def __init__(self, health = 0, health_regen = 0, armor = 0, attack_damage = 0, mana = 0, mana_regen = 0):
        '''Initiates the pokemon, sets instance arguments equal to the init arguments, mana and mana_regen are defaultly None'''
        self.health        = health
        self.health_regen  = health_regen
        self.armor         = armor
        self.attack_damage = attack_damage
        self.mana          = mana
        self.mana_regen    = mana_regen

        self.gold          = 15
        self.items         = []

    def upkeep(self):
        '''This method is called by every pokemon at the start of every turn'''
        self.health += self.health_regen
        self.mana   += self.mana_regen
        self.gold   += 5
        
    def attack(self, other_pokemon):
        '''This is an attack method, where the current pokemon attacks other_pokemon, damage dealt is self.attack_damage - other_pokemon.armor'''
        damage_dealt          = self.attack_damage - other_pokemon.armor
        other_pokemon.health -= damage_dealt

    def rest(self):
        '''This is a method where pokemon rests and regains 10 health.'''
        self.health += 10
    
    def jungle(self):
        '''This method allows pokemon to visit jungle, where different events happen randomly.''' 
        event = randint(1, 4)
        if event == 1:
            print('You found a gold sack +15 gold')
            self.gold += 15
        if event == 2:
            print('You found a lake where you caught a trout +20 health')
            self.health += 20
        if event == 3:
            print('You found the power of meditation +1 health_regen, +2 armor ')
            self.health_regen += 1
            self.armor         = 2
        if event == 4:
            print('You got ambushed by rumble -10 health, -10 gold')
            self.gold   -= 10
            self.health -= 10

    def shop(self):
        '''This method allows pokemon to buy items in a shop that increase its attributes'''
        print('\nWelcome to shop, the following items can be bought:')
        for i in range(len(store.item)):
            print('\n' + store.item[i] + ': ' + store.description[i] + ', ' + str(store.cost[i]) + ' gold' )
        loop_input = input('\nDo you wish to buy any item? y/n ')
        while loop_input == 'y':
            item_input = input('\nWhat item do you wish to buy? ')
            try:
                item_index = store.item.index(item_input)
                item_cost = store.cost[item_index]
                if item_cost <= self.gold:
                    self.gold -= item_cost
                    self.items.append(item_input)
                    print('\nYou bought ' + item_input)
                    print('\nYou now have' + ' ' + str(self.gold) + ' ' + 'gold')
                    self.health        += store.health[item_index]
                    self.health_regen  += store.health_regen[item_index]
                    self.armor         += store.armor[item_index]
                    self.attack_damage += store.attack_damage[item_index]
                    self.mana          += store.mana[item_index]
                    self.mana_regen    += store.mana_regen[item_index]
                else:
                    print('\nNot enough gold!')
                
                loop_input = input('\nWhat item do you wish to buy? y/n ')
            except:
                print('\nThe desired item does not exist!')

#Pokemons definition            
class Pikachu(Pokemon):
    def fireball(self, other_pokemon):
        mana_cost = 60
        if self.mana >= mana_cost:
            other_pokemon.health -= 40
            print('\nCasted Fireball')
        else:
            print('\nNot enough mana!')

class Renekton(Pokemon):
    pass

class Maokai(Pokemon):
    def overgrow(self):
        mana_cost = 20
        if self.mana >= mana_cost:
            self.health        += 5
            self.health_regen  += 1.5
            self.armor         += 0.5
            self.attack_damage += 0.4

        else:
            print('\nNot enough mana!')
    pass

#Creating Instances
store = Store()
info = Info()
pikachu  = Pikachu(140, 8, 5, 15, 100, 20)
renekton = Renekton(150, 10, 10, 20)
maokai = Maokai(170, 10, 5, 10, 120, 10)

#Printing information to players
print_instructions()

input('\nPress enter to view the separate Pokemons!')

print_pokemons()

#Selecting Pokemons
select_pokemons()

#GAME ENGINE
