rooms = {

          0: {"name" : "hall",
              "west" : 'n',
              "east" : 'n',
              "north" : 'n',
              "south" : 1},
}

items = {0: {'name': 'none'},

         1:{'name': 'sword'},

         2:{'name': 'helm'},


}

enemies  = {
         0: {'name': 'mouse'},

         1: {'name': 'rat',
             'attack': 2,
             'defense': 2,
             'health': 2},

         2: {'name': 'ghoul',
             'attack': 4,
             'defense': 3,
             'health': 5},

         3: {'name': 'skeleton',
             'attack': 3,
             'defense': 3,
             'health': 4},

         }
from random import randint

def showTitle():
    print('=========')
#     print('SKELETON QUEST')
#     print('=========')


currentRoom = 0
lastRoom = 0
roomItem = 0
roomEnemy = 0
while True:


    showTitle()

    # roomItem = 0
    # roomEnemy = 0

    print(currentRoom)
    # print(rooms[currentRoom])
    print(lastRoom)

    move = input('direction').lower().split()

    if move[0] in rooms[currentRoom]:
        # currentRoom = rooms[currentRoom][move[0]]


        if rooms[currentRoom][move[0]] not in rooms:

            if lastRoom > currentRoom:
            # if currentRoom not in rooms:
            # lastRoom =
                prevRoom = currentRoom
                rooms[currentRoom][move[0]] = lastRoom + 1
                currentRoom = lastRoom + 1
                # rooms[currentRoom][move[0]] = lastRoom + 1
                print(prevRoom)
                print(currentRoom)

                if move[0] == 'south':
                    rooms[currentRoom] = {'name': 'hallway',  # for lastRoom: rooms[currentRoom} + 1 = etc..
                                          'north': prevRoom}
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['east'] = currentRoom + 1
                        # print(rooms[currentRoom])
                        # print(rooms)
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['west'] = currentRoom + 1
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['south'] = currentRoom + 1
                    # #if no item yet
                    item_chance = randint(1, 10)
                    if item_chance > 7:
                        rooms[currentRoom]['item'] = items[randint(0, 2)]
                        roomItem = rooms[currentRoom]['item']
                    else:
                        roomItem = items[0]['name']
                    # if no enemy yet
                    enemy_chance = randint(1, 10)
                    if enemy_chance > 2:
                        rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                        roomEnemy = rooms[currentRoom]['enemy']
                    else:
                        roomEnemy = enemies[0]['name']

                    print(lastRoom)
                    # print('hahahah')
                    print(rooms[currentRoom])
                    # print(lastRoom)
                    print('hahahah')
                # print(rooms[currentRoom])
                lastRoom = currentRoom

            # else:
            #     print(rooms[currentRoom])
            #     pass
            else:

                currentRoom = rooms[currentRoom][move[0]]
                lastRoom = currentRoom
                print(lastRoom)
                print('lolol')
                if move[0] == 'south':
                    rooms[currentRoom] = {'name': 'hallway',
                                          'north': lastRoom - 1}
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['east'] = lastRoom + 1
                        # print(rooms[currentRoom])
                        # print(rooms)
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['west'] = lastRoom + 1
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['south'] = lastRoom + 1
                    # #if no item yet
                    item_chance = randint(1, 10)
                    if item_chance > 7:
                        rooms[currentRoom]['item'] = items[randint(0, 2)]
                        roomItem = rooms[currentRoom]['item']
                    else:
                        roomItem = items[0]['name']
                    # if no enemy yet
                    enemy_chance = randint(1, 10)
                    if enemy_chance > 7:
                        rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                        roomEnemy = rooms[currentRoom]['enemy']
                    else:
                        roomEnemy = enemies[0]['name']
                if move[0] == 'north':
                    rooms[currentRoom] = {'name': 'hallway',
                                          # 'south': currentRoom + 1,
                                          'south': lastRoom - 1}
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['east'] = lastRoom + 1
                        # print(rooms[currentRoom])
                        # print(rooms)
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['west'] = lastRoom + 1
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['north'] = lastRoom + 1
                    # #if no item yet
                    item_chance = randint(1, 10)
                    if item_chance > 7:
                        rooms[currentRoom]['item'] = items[randint(0, 2)]
                        roomItem = rooms[currentRoom]['item']
                    else:
                        roomItem = items[0]['name']
                    # if no enemy yet
                    enemy_chance = randint(1, 10)
                    if enemy_chance > 7:
                        rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                        roomEnemy = rooms[currentRoom]['enemy']
                    else:
                        roomEnemy = enemies[0]['name']
                if move[0] == 'east':
                    rooms[currentRoom] = {'name': 'hallway',
                                          'west': lastRoom - 1}
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['north'] = lastRoom + 1
                        # print(rooms[currentRoom])
                        # print(rooms)
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['east'] = lastRoom + 1
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['south'] = lastRoom + 1
                    # #if no item yet
                    item_chance = randint(1, 10)
                    if item_chance > 7:
                        rooms[currentRoom]['item'] = items[randint(0, 2)]
                        roomItem = rooms[currentRoom]['item']
                    else:
                        roomItem = items[0]['name']
                    # if no enemy yet
                    enemy_chance = randint(1, 10)
                    if enemy_chance > 7:
                        rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                        roomEnemy = rooms[currentRoom]['enemy']
                    else:
                        roomEnemy = enemies[0]['name']

                if move[0] == 'west':
                    rooms[currentRoom] = {'name': 'hallway',
                                          # 'south': currentRoom + 1,
                                          'east': lastRoom - 1}
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['west'] = lastRoom + 1
                        # print(rooms[currentRoom])
                        # print(rooms)
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['north'] = lastRoom + 1
                    door_chance = randint(1, 1)
                    if door_chance == 1:
                        rooms[currentRoom]['south'] = lastRoom + 1
                    # #if no item yet
                    item_chance = randint(1, 10)
                    if item_chance > 7:
                        rooms[currentRoom]['item'] = items[randint(0, 2)]
                        roomItem = rooms[currentRoom]['item']
                    else:
                        roomItem = items[0]['name']
                    # if no enemy yet
                    enemy_chance = randint(1, 10)
                    if enemy_chance > 7:
                        rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                        roomEnemy = rooms[currentRoom]['enemy']
                    else:
                        roomEnemy = enemies[0]['name']
                    print(rooms[currentRoom])
                else:
                    print(rooms[currentRoom])
                    pass


        else:

            currentRoom = rooms[currentRoom][move[0]]
            print(rooms[currentRoom])

            # if lastRoom > currentRoom:
            #     # if currentRoom not in rooms:
            #     # lastRoom =
            #     prevRoom = currentRoom
            #     rooms[currentRoom][move[0]] = lastRoom + 1
            #     currentRoom = lastRoom + 1
            #     # rooms[currentRoom][move[0]] = lastRoom + 1
            #     print(prevRoom)
            #     print(currentRoom)
            #
            #     if move[0] == 'south':
            #         rooms[currentRoom] = {'name': 'hallway',  # for lastRoom: rooms[currentRoom} + 1 = etc..
            #                               'north': prevRoom}
            #         door_chance = randint(1, 3)
            #         if door_chance == 1:
            #             rooms[currentRoom]['east'] = currentRoom + 1
            #             # print(rooms[currentRoom])
            #             # print(rooms)
            #         door_chance = randint(1, 3)
            #         if door_chance == 1:
            #             rooms[currentRoom]['west'] = currentRoom + 1
            #         door_chance = randint(1, 3)
            #         if door_chance == 1:
            #             rooms[currentRoom]['south'] = currentRoom + 1
            #         # #if no item yet
            #         item_chance = randint(1, 10)
            #         if item_chance > 7:
            #             rooms[currentRoom]['item'] = items[randint(0, 2)]
            #             roomItem = rooms[currentRoom]['item']
            #         else:
            #             roomItem = items[0]['name']
            #         # if no enemy yet
            #         enemy_chance = randint(1, 10)
            #         if enemy_chance > 2:
            #             rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
            #             roomEnemy = rooms[currentRoom]['enemy']
            #         else:
            #             roomEnemy = enemies[0]['name']
            #
            #         print(lastRoom)
            #         # print('hahahah')
            #
            #         print(lastRoom)
            #         print('hahahah')
            #
            #     else:
            #         currentRoom = rooms[currentRoom][move[0]]
            # lastRoom =

        #
        # if move[0] not in rooms:

            # currentRoom = rooms[currentRoom][move[0]]


        # elif move[0] == 'east':
        #     rooms[currentRoom] = {'name': 'hallway',
        #                           # 'south': currentRoom + 1,
        #                           'west': currentRoom - 1}
        #     door_chance = randint(1, 3)
        #     if door_chance == 1:
        #         rooms[currentRoom]['east'] = 'True'
        #         print(rooms[currentRoom])
        #         print(rooms)
        #     door_chance = randint(1, 3)
        #     if door_chance == 1:
        #         rooms[currentRoom]['west'] = 'True'
        #     door_chance = randint(1, 1)
        #     if door_chance == 1:
        #         rooms[currentRoom]['south'] = 'True'
        #     # #if no item yet
        #     item_chance = randint(1, 10)
        #     if item_chance > 7:
        #         rooms[currentRoom]['item'] = items[randint(0, 2)]
        #         roomItem = rooms[currentRoom]['item']
        #     else:
        #         roomItem = items[0]['name']
        #     # if no enemy yet
        #     enemy_chance = randint(1, 10)
        #     if enemy_chance > 7:
        #         rooms[currentRoom]['enemy'] = enemies[randint(0, 2)]
        #         roomEnemy = rooms[currentRoom]['enemy']
        #     else:
        #         roomEnemy = enemies[0]['name']
        # if move[0] == 'north':
        #     rooms[currentRoom] = {'name': 'hallway',
        #                          'south': currentRoom - 1,
        #                          'north': currentRoom + 1}
        # currentRoom = rooms[currentRoom][move[0]]
        # print(currentRoom)
        # rooms[currentRoom] = {'name': 'hallway',
        #                       'east': 2

        # print('you are in the ' + rooms[currentRoom]['name'])
    # print(roomEnemy)
    # print(roomItem)
    # print()
    else:
        print('cant go that way')

    # if roomEnemy != 'none':
    #     print('you see a ' + roomEnemy['name'])
    # else:
    #     pass
    #
    # if roomItem != 'none':
    #     print('you see a ' + roomItem['name'])
    # else:
    #     pass
        # else:
        #     print()






    # print(rooms[currentRoom])
    # print(currentRoom)