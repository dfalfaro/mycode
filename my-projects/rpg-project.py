#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object"""

import random

def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    Get through the dungeon by
    collecting items and defeating
    the boss!
    ========
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
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])

    # main room
    if currentRoom == 'Main Room' and 'compass' in inventory:
        print('''
        up = Jail Room
        down = Dungeon Entrance
        left = Armory
        right = Eastern Room''')

    # dungeon entrance
    if currentRoom == 'Dungeon Entrance' and 'compass' in inventory:
        print('''
        up = Main Room''')

    # eastern room
    if currentRoom == 'Eastern Room' and 'compass' in inventory:
        print('''
        up = Boss Room
        left = Main Room''')

    # armory
    if currentRoom == 'Armory' and 'compass' in inventory:
        print('''
        up = Basement
        right = Main Room''')

    # basement
    if currentRoom == 'Basement' and 'compass' in inventory:
        print('''
        down = Armory''')

    # key room
    if currentRoom == 'Key Room' and 'compass' in inventory:
        print('''
        right = Northern Room''')

    # northern room
    if currentRoom == 'Northern Room' and 'compass' in inventory:
        print('''
        down = Jail Room
        left = Key Room''')

    # boss room
    if currentRoom == 'Boss Room' and 'compass' in inventory:
        print('''
        up = Treasure Room
        down = Eastern Room''')

    # jail room
    if currentRoom == 'Jail Room' and 'compass' in inventory:
        print('''
        up = Northern Room
        down = Main Room''')
    
    # hints
    if currentRoom == 'Jail Room' and 'item' in rooms['Northern Room'] and 'monster' in rooms['Northern Room']['item']:
        print("I hear something ahead... I should find a weapon")
    
    if currentRoom == 'Eastern Room' and 'item' in rooms['Boss Room'] and 'monster' in rooms['Boss Room']['item']:
        print("I hear something ahead... I should find a weapon")
    
    print("---------------------------")

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Dungeon Entrance': {
        'up': 'Main Room'
    },

    'Main Room': {
        'down': 'Dungeon Entrance',
        'up': 'Jail Room',
        'left': 'Armory',
        'right': 'Eastern Room'
    },

    'Armory': {
        'right': 'Main Room',
        'up': 'Basement',
        'item': 'sword'
    },

    'Basement': {
        'down': 'Armory',
        'item': 'compass'
    },

    'Jail Room': {
        'up': 'Northern Room',
        'down': 'Main Room'
    },

    'Northern Room': {
        'down': 'Jail Room',
        'left': 'Key Room',
        'item': 'monster'
    },

    'Key Room': {
        'right': 'Northern Room',
        'item': 'key'
    },

    'Eastern Room': {
        'left': 'Main Room',
        'up': 'Boss Room',
        'item': 'potion'
    },

    'Boss Room': {
        'up': 'Treasure Room',
        'down': 'Eastern Room',
        'item': 'boss'
    },

    'Treasure Room': {
        'down': 'Boss Room',
        'item' : 'bitcoin'
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
    if move[0] == 'attack':
        #add player attack ranges
        playerDamage = random.randint(0, 35)
        #add monster attack ranges
        monsterDamage = random.randint(0, 25)
        #add boss attack ranges
        bossDamage = random.randint(0, 30)

        #fight against monsters
        if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
            if 'sword' in inventory:
                print('You attack the monster with your sword!')
                monsterHealth -= playerDamage
                if monsterHealth <= 0:
                    print('You defeated the monster with your sword! Well done!')
                    del rooms[currentRoom]['item']
                    monsterHealth = 100
                else:
                    print('The monster has', monsterHealth, 'health left.')
                    print('The monster attacks you back!')
                    playerHealth -= monsterDamage
                    if playerHealth <= 0:
                        print('The monster killed you! Game over!')
                        print('You respawned at the entrance')
                        playerLives -= 1
                        currentRoom = 'Dungeon Entrance'
                        playerHealth = 100
                        monsterHealth = 100
                    else:
                        print('You have', playerHealth, 'health left.')
            else:
                print('You have nothing to attack the monster with! They attacked you!')
                print('You respawned at the entrance')
                currentRoom = 'Dungeon Entrance'

        #fight against boss
        if 'item' in rooms[currentRoom] and 'boss' in rooms[currentRoom]['item']:
            if 'sword' in inventory:
                print('You attack the big monster with your sword!')
                bossHealth -= playerDamage
                if bossHealth <= 0:
                    print('You defeated the monster with your sword! Well done!')
                    del rooms[currentRoom]['item']
                else:
                    print('The big monster has', bossHealth, 'health left.')
                    print('The big monster attacks you back!')
                    playerHealth -= bossDamage
                    if playerHealth <= 0:
                        print('The monster killed you! Game over!')
                        print('You respawned at the entrance')
                        playerLives -= 1
                        currentRoom = 'Dungeon Entrance'
                        playerHealth = 100
                        bossHealth = 100
                    else:
                        print('You have', playerHealth, 'health left.')
            else:
                print('You have nothing to attack the big monster with! They attacked you!')
                print('You respawned at the entrance')
                currentRoom = 'Dungeon Entrance'

        else:
            print('You can\'t do that right now')

    # if they type 'go' first
    elif move[0] == 'go':
        if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
            print('Their\'s a monster blocking the way!')
            continue
        if 'item' in rooms[currentRoom] and 'boss' in rooms[currentRoom]['item']:
            print('Their\'s a big monster blocking the way!')
            continue
    # check that they are allowed wherever they want to go
        if len(move) < 2:
            print("Invalid input. Please enter a valid direction.")
            continue
        if move[1] in rooms[currentRoom]:
            # Check if the player is trying to move to the Treasure Room
            if rooms[currentRoom][move[1]] == 'Treasure Room':
                # If they have the key, allow them to move to the Treasure Room
                if 'key' in inventory:
                    currentRoom = rooms[currentRoom][move[1]]
                # Otherwise, print a message informing the player that they need the key to enter the room
                else:
                    print('You need the key to enter the Treasure Room!')
            # If they are trying to move to a different room, set the current room to the new room
            else:
                currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    elif move[0] == 'get':
        if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
            print('Their\'s a monster blocking the way!')
            continue
        if 'item' in rooms[currentRoom] and 'boss' in rooms[currentRoom]['item']:
            print('Their\'s a big monster blocking the way!')
            continue
        if len(move) < 2:
            print("Invalid input. Please enter a valid item to get.")
            continue
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to the inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

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

    # if they run out of lives
    if playerLives <= 0:
        print('You lost all your lives')
        print('GAME OVER')
        break


    # Define how a player can win
    if 'bitcoin' in inventory:
        print('You defeated the monster and got 1 million bitcoin... YOU WIN!')
        break
