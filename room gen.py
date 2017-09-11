from random import randint



def showStatus():
#     print('you are in the ' + rooms[currentRoom]['name'])
    print('---------------')
#     if 'item' in rooms[currentRoom]:
#         print('you see a ' + rooms[currentRoom]['item'])
#     print('---------------')
#     if 'enemy' in rooms[currentRoom]:
#         currentEnemy = rooms[currentRoom]['enemy']
#         # print(currentEnemy)#take out
#         print('you see a ' + rooms[currentRoom]['enemy'])
#     print('---------------')
#     # if move == 'a':
#     rooms[1]['item'] = items[randint(1, 2)]
#     rooms[1]['monster'] = monsters[randint(1, 2)]
#     print(rooms)

# showStatus()
# from random import randint



rooms = {1:{
          'name': 'Dungeon',
         'item': 'n',
         'monster': 'n'},
         # 'south': 1,
         # 'west': 1,
         # 'north': 1,
         # 'east': 1},

}

items = {0: {'name': 'none'},

         1:{'name': 'sword'},

         2:{'name': 'helm'},


}

monsters = {1: {'name': 'rat'},

         2: {'name': 'ghoul'},

         }

currentRoom = 1
roomItem = 'n'

while True:

    showStatus()




    rooms[1]['item'] = items[randint(0, 2)]
    roomItem = rooms[currentRoom]['item']
    rooms[1]['monster'] = monsters[randint(1, 2)]
    roomMonster = rooms[currentRoom]['monster']
    print(rooms)

    print('you are in the ' + rooms[currentRoom]['name'])

    print('you see a ' + roomMonster['name'])

    if roomItem != 'none':
        print('you see a ' + roomItem['name'])
    # else:
    #     print()
    print(roomItem)
    move = input('>>>')
    if move == 'a':
        pass