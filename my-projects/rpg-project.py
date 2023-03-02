#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object"""

import random

def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
           Dungeon Warrior I
    ==============================
    Get through the dungeon by
    collecting items and defeating
    the boss!
    ==============================
    Commands:
    go [direction]
    get [item]
    attack
    heal
    quit
    ''')


def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Health:', playerHealth)
    print('Lives:', playerLives)
    print('Inventory:', inventory)

    # main room
    if currentRoom == 'Main Room' and 'compass' in inventory:
        print('''
        up = Jail Room
        down = Dungeon Entrance
        left = Armory
        right = Goblin\'s Kitchen
        ''')

    # dungeon entrance
    if currentRoom == 'Dungeon Entrance' and 'compass' in inventory:
        print('''
        up = Main Room
        ''')

    # goblin kitchen
    if currentRoom == 'Goblin\'s Kitchen' and 'compass' in inventory:
        print('''
        up = Ogre\'s Cave
        left = Main Room
        ''')
        if 'battle-axe' in inventory:
            print('A mysterious old man appears in front of you...')
            print('Old Man: You found the secret room!')
        else:   
            print('A mysterious old man appears in front of you...')
            print("Old Man: Don't always rely on the compass...")

    # armory
    if currentRoom == 'Armory' and 'compass' in inventory:
        print('''
        up = Basement
        down = Garden
        right = Main Room
        ''')
        if 'compass' in inventory:
            print('A mysterious old man appears in front of you...')
            print('Old Man: You found my old compass!')
        else:   
            print('A mysterious old man appears in front of you...')
            print("Old Man: Those dang monsters stole my most precious item...")

    # basement
    if currentRoom == 'Basement' and 'compass' in inventory:
        print('''
        down = Armory
        ''')

    # key room
    if currentRoom == 'Key Room' and 'compass' in inventory:
        print('''
        right = Northern Room
        ''')

    # northern room
    if currentRoom == 'Northern Room' and 'compass' in inventory:
        print('''
        down = Jail Room
        left = Key Room
        ''')

    # ogre's cave
    if currentRoom == 'Ogre\'s Cave' and 'compass' in inventory:
        print('''
        up = Hero\'s Sanctuary
        down = Goblin\'s Kitchen
        left = Jail Room
        ''')

    # jail room
    if currentRoom == 'Jail Room' and 'compass' in inventory:
        print('''
        up = Northern Room
        down = Main Room
        right = Ogre\'s Cave
        ''')

    #Hero's sanctuary
    if currentRoom == 'Hero\'s Sanctuary' and 'compass' in inventory:
        print('''
        down = Orge\'s Cave
        right = Troll Hall
        ''')

    #Garden
    if currentRoom == 'Garden' and 'compass' in inventory:
        print('''
        up = Armory
        ''')

    #Troll Hall
    if currentRoom == 'Troll Hall' and 'compass' in inventory:
        print('''
        down = Dragon\'s Gate
        left = Hero\'s Sanctuary
        ''')

    #Dragon Gate
    if currentRoom == 'Dragon\'s Gate' and 'compass' in inventory:
        print('''
        up = Troll Hall
        down = Dragon\'s Nest
        left = Hole
        ''')

    #Dragon nest
    if currentRoom == 'Dragon\'s Nest' and 'compass' in inventory:
        print('''
        down = Treasure Room
        up = Dragon\'s Gate
        ''')   

    #secret room
    if currentRoom == 'Secret Room' and 'compass' in inventory:
        print('''
        up = Goblin\'s Kitchen
        ''') 

    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    if 'enemy' in rooms[currentRoom]:
        print('A ' + rooms[currentRoom]['enemy'] + ' is attacking you')
    if 'boss' in rooms[currentRoom]:
        print('A ' + rooms[currentRoom]['boss'] + ' is staring down at you...')
    
    print("---------------------------")

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Dungeon Entrance': {
        'up': 'Main Room',
        'item': 'sword'
    },

    'Main Room': {
        'down': 'Dungeon Entrance',
        'up': 'Jail Room',
        'left': 'Armory',
        'right': 'Goblin\'s Kitchen',
        'enemy': 'monster'
    },

    'Armory': {
        'right': 'Main Room',
        'up': 'Basement',
        'down': 'Garden',
    },

    'Garden': {
        'up': 'Armory',
        'enemy': 'monster'
    },

    'Basement': {
        'down': 'Armory',
    },

    'Jail Room': {
        'up': 'Northern Room',
        'right': 'Ogre\'s Cave',
        'down': 'Main Room'
    },

    'Ogre\'s Cave': {
        'left': 'Jail Room',
        'up': 'Hero\'s Sanctuary',
        'down': 'Goblin\'s Kitchen',
        'enemy': 'monster',
    },

    'Hero\'s Sanctuary': {
        'down': 'Ogre\'s Cave',
        'right': 'Troll Hall',
        'item': 'potion'
    },

    'Northern Room': {
        'down': 'Jail Room',
        'left': 'Key Room',
        'enemy': 'monster',
    },

    'Key Room': {
        'right': 'Northern Room',
        'item': 'key'
    },

    'Goblin\'s Kitchen': {
        'left': 'Main Room',
        'up': 'Ogre\'s Cave',
        'down': 'Secret Room',
        'item': 'potion'
    },

    'Dragon\'s Nest': {
        'down': 'Treasure Room',
        'up': 'Dragon\'s Gate',
        'boss': 'Dragon'
    },

    'Dragon\'s Gate': {
        'up': 'Troll Hall',
        'down': 'Dragon\'s Nest',
        'left': 'hole',
        'item': 'potion'
    },

    'Troll Hall': {
        'left': 'Hero\'s Sanctuary',
        'down': 'Dragon\'s Gate',
        'enemy': 'monster'
    },

    'Treasure Room': {
        'item' : 'bitcoin'
    },

    'Secret Room': {
        'up': 'Goblin\'s Kitchen',
        'item': 'battle-axe'
    }

}

# start the player in the entrance
currentRoom = 'Dungeon Entrance'

#add player health
playerHealth = 100

#add player lives
playerLives = 3

#add monster health
monsterHealth = 100

#add boss health
bossHealth = 150

#add player attack ranges
playerDamage = random.randint(0, 20)

#if player has a weapon, they're stronger
if 'sword' in inventory:
    playerDamage = random.randint(0, 35)   
if 'battle-axe' in inventory:
    playerDamage = random.randint(0, 45)    

#add monster attack ranges
monsterDamage = random.randint(0, 25)

#add boss attack ranges
bossDamage = random.randint(0, 30)


showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # normalize input and check length
    move = move.lower().split(" ")
    if len(move) < 1:
        print("Invalid input. Please enter a valid command.")
        continue

    # if they type 'attack'
    elif move[0] == 'attack':
        #fight against monsters
        if 'enemy' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['enemy']:
            print('You attacked the monster!')
            monsterHealth -= playerDamage
            if monsterHealth <= 0:
                print('You defeated the monster! Well done')
                del rooms[currentRoom]['enemy']
                monsterHealth = 100
                if 'compass' not in inventory:
                    if random.randint(1, 100) <= 25:  # 20% chance of dropping a compass
                        print('They dropped a compass!')
                        inventory.append('compass')                  
            else:
                print('The monster has', monsterHealth, 'health left.')
                print('The monster attacks you back!')
                playerHealth -= monsterDamage
                if playerHealth <= 0:
                    if playerLives <= 1:
                        print('The monster killed you!')
                        print('You lost all your lives')
                        print('GAME OVER')
                        break
                    else:
                        print('The monster killed you!')
                        print('You respawned at the entrance')
                        playerLives -= 1
                        currentRoom = 'Dungeon Entrance'
                        playerHealth = 100
                        monsterHealth = 100
                else:
                    print('You have', playerHealth, 'health left.')
        else:
            print('There\'s nothing to attack')

        #fight against boss
        if 'boss' in rooms[currentRoom] and 'Dragon' in rooms[currentRoom]['boss']:
            print('You attacked the Dragon!')
            bossHealth -= playerDamage
            if bossHealth <= 0:
                print('You defeated the Dragon! Well done!')
                del rooms[currentRoom]['boss']
            else:
                print('The Dragon has', bossHealth, 'health left.')
                print('The Dragon attacks you back!')
                playerHealth -= bossDamage
                if playerHealth <= 0:
                    if playerLives <= 1:
                        print('The Dragon killed you!')
                        print('You lost all your lives')
                        print('GAME OVER')
                        break
                    else:
                        print('The Dragon killed you!')
                        print('You respawned at the entrance')
                        playerLives -= 1
                        currentRoom = 'Dungeon Entrance'
                        playerHealth = 100
                        bossHealth = 150
                else:
                    print('You have', playerHealth, 'health left.')

    # if they type 'go' first
    elif move[0] == 'go':
        if 'enemy' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['enemy']:
            print('A monster is attacking you!')
            continue
        if 'boss' in rooms[currentRoom] and 'Dragon' in rooms[currentRoom]['boss']:
            print('The Dragon is attacking you!')
            continue
    # check that they are allowed wherever they want to go
        if len(move) < 2:
            print("Invalid input. Please enter a valid direction.")
            continue
        if move[1] in rooms[currentRoom]:
            # Check if the player is trying to move to the Treasure Room
            if rooms[currentRoom][move[1]] == 'Dragon\'s Nest':
                # If they have the key, allow them to move to the Treasure Room
                if 'key' in inventory:
                    currentRoom = rooms[currentRoom][move[1]]
                # Otherwise, print a message informing the player that they need the key to enter the room
                else:
                    print('You need a key to unlock the gate!') 
            elif rooms[currentRoom][move[1]] == 'hole':
                print('You fell into a hole and are back at the entrance!')          
                currentRoom = 'Dungeon Entrance'
            # If they are trying to move to a different room, set the current room to the new room
            else:
                currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    elif move[0] == 'get':
        if 'enemy' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['enemy']:
            print('A monster is attacking you!')
            continue
        if 'boss' in rooms[currentRoom] and 'Dragon' in rooms[currentRoom]['boss']:
            print('The Dragon is attacking you!')
            continue
        if len(move) < 2:
            print("Invalid input. Please enter a valid item to get.")
            continue
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] == rooms[currentRoom]['item']:
            # add the item to the inventory
            inventory += [move[1]]
            # display a helpful message
            print('You got a ' + move[1] + '!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        else:
            # tell them they can't get it
            print('I don\'t see a ' + move[1] + '!')
        

    # healing with potion
    elif move[0] == 'heal':
        if "potion" in inventory:
            if playerHealth == 100:
                print('Your health is full')
            else:
                playerHealth = 100
                print('you regenerated your health!')
                inventory.remove('potion')
        else:
            print("You have no potions")

    # if they type 'quit'
    elif move[0] == 'quit':
        # print a message and break the loop
        print('Quitting game...')
        break

    # if they type anything else
    else:
        print('Invalid command! Please try again.')

    # Define how a player can win
    if 'bitcoin' in inventory:
        print('You defeated the monster and got 1 million bitcoin... YOU WIN!')
        break
