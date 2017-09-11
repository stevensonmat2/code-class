import random
from random import randint



def ran_room():
    done_doors = []
    chosen_doors = []
    while True:
        potential_doors = ['north', 'south', 'east', 'west']
        door_choice = potential_doors.pop(random.randint(0, len(potential_doors)-1))
        done_doors.append(door_choice)
        door_chance = randint(1,3)
        print(door_chance)
        if door_chance == 1 or door_chance == 2:
            chosen_doors.append(door_choice)
        if len(done_doors) == len(potential_doors):
            break



    print(chosen_doors)

ran_room()