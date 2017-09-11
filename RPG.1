def showInstructions():
    print('=========')
    print('SKELETON QUEST')
    print('=========')
    print('Commands: ')
    print('To move type: "go [direction]"')
    print('To get item: "take [item]"')
    print('To equip item: "equip [item]"')
    print('To fight enemy: "fight with [item]"')
    print('---------------')
    # print('To show map: "show [maps]"')

def showStatus():
    print('you are in the ' + rooms[currentRoom]['name'])
    print('---------------')
    if 'item' in rooms[currentRoom]:
        print('you see a ' + rooms[currentRoom]['item'])
    print('---------------')
    if 'enemy' in rooms[currentRoom]:
        currentEnemy = rooms[currentRoom]['enemy']
        # print(currentEnemy)#take out
        print('you see a ' + rooms[currentRoom]['enemy'])
    print('---------------')

inventory = ['sword']

items = {
         'sword': {'name': 'sword',
                    'attack' : 2},
         'hat': {'name': 'hat'}

        }
enemies = {
           'skeleton': {'name': 'skeleton',
                        'health': 4,
                        'attack': 1}

          }

rooms = {

          1: {"name" : "hall",
              "east" : 2,
              "north" : 5,
              "south" : 3},

          2: {"name" : "bedroom",
              "west" : 1,
              "south" : 4,
              'item' : 'sword'},

          3: {"name" : "kitchen",
              "north" : 1},

          4: {"name" : "bathroom",
              "north" : 2},

          5: {"name" : "dungeon",
              "south" : 1,
              "enemy" : "skeleton"}

        }


currentRoom = 5
currentEnemy = 'n'
currentWeap = 'n'
currentArm = 'n'
currentHelm = 'n'
currentSpell = 'n'

playerHealthMax = 8
playerHealthCurr = 8
enemyHealth = 1

showInstructions()

while True:

    showStatus()

    move = input(">enter command: ").lower().split()

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('---------------')
            print('you cant go that way!')
            print('---------------')

    if move[0] == 'take':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' obtained!')
            del rooms[currentRoom]['item']
            # inventory[item] = item

        else:
            print('you already took ' + move[1] + '!')

    if move[0] == 'show' and move[1] == 'inventory':
        print(inventory)

    if move[0] == 'equip':
        if move[1] in inventory:
            currentWeap = move[1]
            print('---------------')
            print(currentWeap + ' equipped!')
            print('---------------')
        elif move[1] not in items:
            print('---------------')
            print('that aint real')
            print('---------------')
        else:
            print('---------------')
            print('you dont have that item')
            print('---------------')


    if move[0] == 'fight':
        if 'enemy' in rooms[currentRoom]:

            currentEnemy = rooms[currentRoom]['enemy']
            enemyHealth = enemies[currentEnemy]['health']
            # print(enemyHealth)#take out
            if 'enemy' in rooms[currentRoom] and currentWeap != 'n':
                print('you hit ' + rooms[currentRoom]['enemy'] + ' with ' +  [currentWeap])
                enemyHealth = enemies[currentEnemy]['health'] - items[currentWeap]['attack']
                print('enemy HP = ')
                print(enemyHealth)
                if [enemyHealth] == 0:
                    del rooms[currentRoom]['enemy']
                    pass
                else:
                    print(rooms[currentRoom]['enemy'] + ' fights back!')
                    playerHealthCurr = playerHealthMax - enemies[currentEnemy]['attack']
                    print('player HP = ')
                    print([playerHealthCurr])

                # print(enemyHealth)
            else:
                print('***************')
                print('WEAPON NOT EQUIPPED')
                print('***************')
                continue

            query = input('Hit Again? (y/n): ')
            if query == 'y':
                enemyHealth = enemyHealth - items[currentWeap]['attack']
            if query == 'n':
                print('run away!')
            if enemyHealth == 0:
                print(rooms[currentRoom]['enemy'] + ' slain!')
                del rooms[currentRoom]['enemy']
                # rooms[currentRoom]['item']['hat']
        # if enemies[currentEnemy]['health'] <= items[currentWeap]['attack']:
            # print(rooms[currentRoom]['enemy'] + ' slain!')
                # print([currentEnemy])#take out
                # del rooms[currentRoom]['enemy']
                # enemyHealth = 1
                # print(enemyHealth)#take out

  # if enemies[currentEnemy]['health'] <=
        #     print('skeleton slain')
        #     del rooms[currentRoom]['enemy']
        # else:
        #     print('You do not have that weapon')


 # print('you are in room ' + currentRoom)
 # print('this is the ' + rooms[currentRoom]['name'])
 # move = input('>')
 # currentRoom = rooms[currentRoom][move]
 # print('you are now in room ' + currentRoom)
 # print('this is the' + rooms[currentRoom]['name'])
