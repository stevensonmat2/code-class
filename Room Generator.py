from random import randint

rooms = {1:{'item': 'n',
         'monster': 'n',
         'south': 1,
         'west': 1,
         'north': 1,
         'east': 1},

}


items = {1:{'name': 'sword'},

         2:{'name': 'helm'},


}

monsters = {1: {'name': 'rat'},

         2: {'name': 'ghoul'},

         }


currentRoom = 1

open_close = 1

move = input('go').lower().split()

if move == 'go':

    from random import randint
    rooms[currentRoom]['item'] = items[randint(1,2)]
    rooms[currentRoom]['monster'] = monsters[randint(1,2)]
if rooms[currentRoom]['south'] == move[1]:
    rooms[currentRoom]['north'] = '1'
else: rooms[currentRoom]['north'] = randint(1, 2)

# else:
# if rooms[currentRoom]['wall1'] == move[1]:
#    rooms[currentRoom]['wall4'] = 'north'
# else:
#     pass
    # rooms[currentRoom]['wall2'] =
    # rooms[currentRoom]['wall3'] =
    # rooms[currentRoom]['wall4'] =
print(rooms[currentRoom])