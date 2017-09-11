def showInstructions():
    print('=========')
    print('SKELETON QUEST')
    print('=========')
    print('Commands: ')
    print('---------------')
    print('To move type: "go [direction]"')
    print('To get item: "take [item]"')
    print('To equip item: "equip [item]"')
    print('To fight enemy: "fight"')
    print('To see inventory: "inv"')
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

# divie items into weap_items, wear_items, and use_items
# weapons should do different damage to different enemy types
items = {
         'sword': {'name': 'sword',
                    'attack': 1},
         'potion': {'name': 'potion',
                    'restore': 4},
         'helm': {'name': 'helm',
                        'defense': 2},

        }
enemies = {
           'skeleton': {'name': 'skeleton',
                        'type': 'skeleton',
                        'health': 4,
                        'attack': 1,
                        'item': 'potion'},

           'giant skeleton': {'name': 'giant skeleton',
                              'type': 'skeleton',
                              'health': 8,
                              'attack': 2,
                              'item': 'helm'},

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
              "north" : 6,
              "enemy" : "skeleton"},

          6: {"name" : "lair",
              "south" : "5",
              "east" : 7,
              "enemy" : "giant skeleton"}

        }


currentRoom = 5
currentEnemy = 'n'
currentWeap = 'n'
currentArm = 'n'
currentHelm = 'n'
currentSpell = 'n'

playerHealthMax = 8
playerHealthNow = 8
playerHealthCurr = 8
enemyHealthNow = 1
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

    if move[0] == 'inv':
        print('---------------')
        print('Inventory: ' + str(inventory))
        print('---------------')
        query = input('type "[item]" for details or "exit": ')
        if query in inventory:
            print('---------------')
            print(items[query])
        else:
            pass
            print('---------------')

    if move[0] == 'take':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' obtained!')
            del rooms[currentRoom]['item']
            # inventory[item] = item

        else:
            print('---------------')
            print('there is no ' + move[1] + '!')
            print('---------------')
    # if move[0] == 'show' and move[1] == 'inventory':
    #     print('Inventory = ' + str(inventory))

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


    # else:
    #     print('choose item to equip')

    if move[0] == 'fight':
        print('---------------')
        if 'enemy' in rooms[currentRoom]:

            currentEnemy = rooms[currentRoom]['enemy']
            # enemyHealth = enemies[currentEnemy]['health']
            # print(enemyHealth)#take out
            if 'enemy' in rooms[currentRoom] and currentWeap != 'n':
                print('you hit ' + rooms[currentRoom]['enemy'] + ' with ' + str(currentWeap))
                enemyHealth = enemies[currentEnemy]['health'] - items[currentWeap]['attack']
                print('---------------')
                print('enemy HP = ' + str(enemyHealth))
                print('---------------')
            else:
                print('***************')
                print('NO WEAPON EQUIPPED')
                print('***************')
                continue
                # print(enemyHealth)
            if enemyHealth == 0:
                print(rooms[currentRoom]['enemy'] + ' slain!')
                rooms[currentRoom]['item'] = enemies[currentEnemy]['item']
                print(enemies[currentEnemy]['item'])
                del rooms[currentRoom]['enemy']
                    # print(rooms[currentRoom]['enemy'] + ' slain!')

            else:
                print('---------------')
                print(rooms[currentRoom]['enemy'] + ' fights back!')
                print('---------------')
                playerHealthCurr = playerHealthNow - enemies[currentEnemy]['attack']
                playerHealthNow = playerHealthCurr
                print('---------------')
                print('player HP = ' + str(playerHealthCurr))
                print('---------------')
                query = input('Hit Again? (y/n): ')
                print('---------------')
                if enemyHealth > 0:
                    if query == 'y':
                        enemyHealth = enemyHealth - items[currentWeap]['attack']
                        if enemyHealth == 0:
                            print(rooms[currentRoom]['enemy'] + ' slain!')
                            print('---------------')
                            rooms[currentRoom]['item'] = enemies[currentEnemy]['item']
                            print('---------------')
                            print(enemies[currentEnemy]['item'])
                            print('---------------')
                            del rooms[currentRoom]['enemy']
                            print('---------------')
                        else:
                            continue
                    if query == 'n':
                        print('run away!')


        else:
            print('---------------')
            print('nothing to fight here')
            print('---------------')# else:
                #     pass
                    # print([playerHealthCurr])

                # print(enemyHealth)
            # else:
            #     print('***************')
            #     print('NO WEAPON EQUIPPED')
            #     print('***************')
            #     continue

            # query = input('Hit Again? (y/n): ')
            # print('---------------')
            # if query == 'y':
            #     enemyHealth = enemyHealth - items[currentWeap]['attack']
            #     if enemyHealth == 0:
            #         print(rooms[currentRoom]['enemy'] + ' slain!')
            #         print('---------------')
            #         del rooms[currentRoom]['enemy']
            #         print('---------------')
            #
            #     else:
            #         continue



                # if query == 'n':
                #     print('run away!')
            # if enemyHealth == 0:
            #     print(rooms[currentRoom]['enemy'] + ' slain!')
            #     del rooms[currentRoom]['enemy']
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
