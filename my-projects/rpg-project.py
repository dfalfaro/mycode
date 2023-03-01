#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Get to the Garden with
    a key and a potion to
    win! Avoid the monsters!
    ========
    Commands:
      go [direction]
      get [item]
      attack
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

def attack():
    """attack the monster if in the room"""
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        if 'sword' in inventory:
            print('You defeated the monster with your sword! Well done!')
            del rooms[currentRoom]['item']
        else:
            print('You have nothing to attack the monster with! Run!')
    else:
        print('There is no monster in this room!')

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Bedroom',
                  'item'  : 'sword'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'potion'
                },
            'Bedroom' : {
                  'east' : 'Hall',
                  'item' : 'key'
               },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'monster'
                  
               },
            'Garden' : {
                  'north' : 'Dining Room'
             }

         }

# start the player in the Hall
currentRoom = 'Hall'

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

        # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if len(move) < 2:
            print("Invalid input. Please enter a valid direction.")
            continue
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    elif move[0] == 'get':
        if len(move) < 2:
            print("Invalid input. Please enter a valid item to get.")
            continue
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        elif "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to the inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if they type 'attack'
    elif move[0] == 'attack':
        attack()

    # if they type 'quit'
    elif move[0] == 'quit':
        # print a message and break the loop
        print('Quitting game...')
        break

    # if they type anything else
    else:
        print('Invalid command! Please try again.')

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has appeared!')
        # check if player has a weapon
        if 'sword' in inventory:
            # if they do, defeat the monster
            print('You defeated the monster with your sword! Well done!')
            del rooms[currentRoom]['item']
        else:
            # if not, the player is defeated
            print('You have nothing to attack the monster with! Run!')
            print('GAME OVER')
            break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

