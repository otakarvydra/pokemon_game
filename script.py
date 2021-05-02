#Modules import
from random import randint

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

        self.gold          = 80
        self.items         = []

    def upkeep(self):
        '''This method is called by every pokemon at the start of every turn, does not contain mana regen, to include mana_regen, inherit and add to this method'''
        self.health = self.health + self.health_regen
        self.gold  += 5
        
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
            print('You got ambushed by rumble -10 gold, -10 health')
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
            
store = Store()