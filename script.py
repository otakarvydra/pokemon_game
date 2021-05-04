#####MODULES IMPORT
from random import randint

#####FUNCTION DEFINITION
def select_pokemons():
    pokemons = ['pikachu', 'renekton', 'maokai']
    global pokemon_2
    global pokemon_1
    pokemon_2 = input('\n----Player 2, please select a pokemon (use lowercase characters only) ')
    pokemon_1 = input('\n----Player 1, please select a pokemon (use lowercase characters only) ')
    while not(pokemon_1 in pokemons and pokemon_2 in pokemons):
        print('\nInvalid pokemon selection')
        pokemon_2 = input('\n----Player 2, please select a pokemon (use lowercase characters only) ')
        pokemon_1 = input('\n----Player 1, please select a pokemon (user lowercase characters only) ')
    pokemon_2 = eval(pokemon_2) 
    pokemon_1 = eval(pokemon_1)

def print_instructions():
    print(info.instructions)

def print_pokemons():
    print('\n' + info.pikachu)
    print('\n' + info.renekton)
    print('\n' + info.maokai)

def state_of_pokemon_1():
    print('\nPokemon 1 attributes:')
    print('  health: '        + str(pokemon_1.health))
    print('  health_regen: '  + str(pokemon_1.health_regen))
    print('  armor: '         + str(pokemon_1.armor))
    print('  attack damage: ' + str(pokemon_1.attack_damage))
    print('  mana: '          + str(pokemon_1.mana))
    print('  mana_regen: '    + str(pokemon_1.mana_regen))
    print('  gold: '          + str(pokemon_1.gold))

def state_of_pokemon_2():

    print('\nPokemon 2 attributes:')
    print('  health: '        + str(pokemon_2.health))
    print('  health_regen: '  + str(pokemon_2.health_regen))
    print('  armor: '         + str(pokemon_2.armor))
    print('  attack damage: ' + str(pokemon_2.attack_damage))
    print('  mana: '          + str(pokemon_2.mana))
    print('  mana_regen: '    + str(pokemon_2.mana_regen))
    print('  gold: '          + str(pokemon_2.gold))

def end_game():
    if pokemon_1.health <= 0:
        print('\nGAME OVER, PLAYER 2 WON! ')

    if pokemon_2.health <= 0:
        print('GAME OVER, PLAYER 1 WON!')

    input('\n----Press enter to exit! ')

#####INFO CLASS DEFINITION
class Info:
    instructions =''' 
Welcome to Pokemon game!
In this game, you and your opponent will choose a Pokemon out of 3 available Pokemons.
The game objective is to defeat the opponents Pokemon. 
The first part of each turn is called the upkeep. Here the pokemons regain their health, mana and gain gold.
Each Pokemon gets 5 gold in the upkeep, health and mana regen are specific to each pokemon.
Pokemons have no maximum health
To make the game fair, player 1 has the first turn, but player turn selects the first pokemon. 
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
        This is specific to every Pokemon, there is one Pokemon that has no ability!'''

    pikachu  ='''
Pikachu:
    Light caster, excels from start, has very high burst potential!
    health        = 140
    health_regen  = 8
    armor         = 5
    attack_damage = 15
    mana          = 100
    mana_regen    = 20

    fireball: Costs 60 mana and deals 40 damage to target Pokemon'''
    
    renekton ='''
Renekton:
    Tough figher, has no abilities, uses brute force to win!
    health        = 150
    health_regen  = 12
    armor         = 10
    attack_damage = 20'''
    
    maokai ='''
Maokai:
    Massive creature, that grows overtime until it can not be stopped!
    health        = 170
    health_regen  = 10
    armor         = 5
    attack_damage = 10
    mana          = 120
    mana_regen    = 10
 
    overgrow: Costs 20 mana and Maokai gains 5 health, 1.5 health_regen, 0.5 armor and 0.4 attack_damage'''

#####STORE CLASS DEFINITION
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

#####GENERAL POKEMON CLASS DEFINITION
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
            print('\nYou found a gold sack +15 gold')
            self.gold += 15
        if event == 2:
            print('\nYou found a lake where you caught a trout +20 health')
            self.health += 20
        if event == 3:
            print('\nYou found the power of meditation +1 health_regen, +2 armor ')
            self.health_regen += 1
            self.armor        += 2
        if event == 4:
            print('\nYou got ambushed by rumble -10 health, -10 gold')
            self.gold   -= 10
            self.health -= 10

    def shop(self):
        '''This method allows pokemon to buy items in a shop that increase its attributes'''
        print('\n----SHOP----')
        items_bought = 0
        for i in range(len(store.item)):
            print('\n' + store.item[i] + ': ' + store.description[i] + ', ' + str(store.cost[i]) + ' gold' )
        loop_input = input('\n----Do you wish to buy any item? y/n ')
        while loop_input == 'y':
            item_input = input('\n----What item do you wish to buy? ')
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
                    items_bought       += 1
            
                else:
                    print('\nNot enough gold!')
                
                loop_input = input('\n----Do you wish to buy any item? y/n ')
            except:
                print('\nThe desired item does not exist!')
        
        if loop_input != 'y':
            print('\nLeaving shop!')
           
        if items_bought > 0:
            return True
        else:
            return False

#####INDIVIDUAL POKEMON DEFINITION          
class Pikachu(Pokemon):
    def __repr__(self):
        return 'Fireball: Costs 60 mana, deals 40 damage to target pokemon. '

    def fireball(self, other_pokemon):
        mana_cost = 60
        if self.mana >= mana_cost:
            self.mana -= mana_cost
            other_pokemon.health -= 40
            print('\nCasted Fireball!')
            return True
        else:
            print('\nNot enough mana!')
            print('\nEnter your action again! ')
            return False

class Renekton(Pokemon):
    def __repr__(self):
        return 'No ability'
       
class Maokai(Pokemon):
    def __repr__(self):
        return 'Overgrow: Costs 20 mana, health + 5, health_regen: + 1.5, armor + 0.5, attack_damage + 0.4 '

    def overgrow(self):
        mana_cost = 20
        if self.mana >= mana_cost:
            self.mana -= mana_cost
            self.health        += 5
            self.health_regen  += 1.5
            self.armor         += 0.5
            self.attack_damage += 0.4
            print('\nCasted overgrow! ')
            return True
        else:
            print('\nNot enough mana! ')
            print('\nEnter your action again! ')
            return False
    pass

#####CREATING INSTANCES
store = Store()
info = Info()
pikachu  = Pikachu(140, 8, 5, 15, 100, 20)
renekton = Renekton(150, 10, 10, 20)
maokai = Maokai(170, 10, 5, 10, 120, 10)

#####PRINTING INFORMATION TO PLAYERS
print_instructions()

input('\n----Press enter to view the separate Pokemons! ')

print_pokemons()

#####SELECTING POKEMONS
select_pokemons()

#####GAME ENGINE LOGIC
turn_number = 0

while (pokemon_1.health > 0 and pokemon_2.health > 0):
    turn_number += 1 
    if turn_number % 2 == 1:
        if turn_number > 1:
            state_of_pokemon_1()
            state_of_pokemon_2()
            pokemon_1.upkeep()
        input('\n----Press enter for next turn! ')
        print('\n----------TURN ' + str(turn_number) + '----------')
        state_of_pokemon_1()
        print('\n' + repr(pokemon_1))
        state_of_pokemon_2()
        print('\n' + repr(pokemon_2))
        print("\nPlayer 1! ")

        while True:
            user_input = input('\n----What do you wish to do? A - attack, J - Jungle, R - rest, S - shop, C - cast ability ')
            if user_input == 'A':
                pokemon_1.attack(pokemon_2)
                print('\nPlayer 1 attacked player 2! ')
                break
            if user_input == 'J':
                pokemon_1.jungle()
                break
            if user_input == 'R':
                pokemon_1.rest()
                print('\nPlayer 1 rested. ')
                break
            if user_input == 'S':
                skip = pokemon_1.shop()
                if skip == True:
                    break
            if user_input == 'C':
                if type(pokemon_1) == Maokai:
                    skip = pokemon_1.overgrow()
                    if skip == True:
                        break
                if type(pokemon_1) == Pikachu:
                    skip = pokemon_1.fireball(pokemon_2)
                    if skip == True:
                        break
                if type(pokemon_1) == Renekton:
                    print('\nRenekton has no ability, choose another action! ')
            else:
                print('\nEnter your action again! ')
    else:
        state_of_pokemon_1()
        state_of_pokemon_2()
        if turn_number > 2:
            pokemon_2.upkeep()
        input('\n----Press enter for next turn! ')
        print('\n----------TURN ' + str(turn_number) + '----------')
        state_of_pokemon_1()
        print('\n' + repr(pokemon_1))
        state_of_pokemon_2()
        print('\n' + repr(pokemon_2))
        print("\nPlayer 2! ")

        while True:
            user_input = input('\n----What do you wish to do? A - attack, J - Jungle, R - rest, S - shop, C - cast ability ')
            if user_input == 'A':
                pokemon_2.attack(pokemon_1)
                print('\nPlayer 2 attacked player 1! ')
                break
            if user_input == 'J':
                pokemon_2.jungle()
                break
            if user_input == 'R':
                pokemon_2.rest()
                print('\nPlayer 2 rested. ')
                break
            if user_input == 'S':
                skip = pokemon_2.shop()
                if skip == True:
                    break
            if user_input == 'C':
                if type(pokemon_2) == Maokai:
                    skip = pokemon_2.overgrow()
                    if skip == True:
                        break
                if type(pokemon_2) == Pikachu:
                    skip = pokemon_2.fireball(pokemon_1)
                    if skip == True:
                        break
                if type(pokemon_2) == Renekton:
                    print('\nRenekton has no ability, choose another action! ')
            else:
                print('\nEnter your action again! ')

#####ENDING THE GAME
end_game()