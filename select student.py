from random import randint

students = {

1: {'Kasey'},
2: {'Tom'},
3: {'Pablo'},
4: {'Brett'},
5: {'Dana'},
6: {'Matt'},
7: {'Jeff'},
8: {'Mike'},
9: {'johnny'},
10: {'Michelle'}



}

name = input('type "s": ')
remove = 0

def pick_name():

    while True:
        if name == 's':
            remove = randint(1, 12)
            if remove in students:
                print(students[remove])
                del students[remove]
                # print(students)
            else:
                pass
pick_name()
