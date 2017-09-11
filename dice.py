#
#
# query = input('what kind of die? (6, 10, or 20 sided)')
# if query == '6':
#     import random
#     def main ():
#         min = 1
#         max = 6
#         roll_again = 'yes'
#         while roll_again == 'yes' or roll_again == 'y':
#             print(random.randint(min, max))
#             main()


roll_again = "yes"

while roll_again == "yes" or roll_again == "y":

    dice_num = input('How many dice?: ')
    def die_count(dice_num):
        # print('number of dice: ' + dice_num)

        die_count(dice_num)


    d_type = input('What number of sides?: ')
    def dice_type(d_type):
        print(dice_num + ' ' + d_type + '-sided dice')


    dice_type(d_type)

    def dice_rolls():


        Dice = d_type
        dice = dice_num
        from random import randint
        for dice in range(1, (int(dice) + 1)):
            print(randint(1, int(Dice)))
            # continue

        roll_again = input("Try again? Yes or No: ").lower

    dice_rolls()





# def dice_results():
#
#     # dice_num_list = []
#     # dice_num_list.append(die_count(dice_num))
#
#     print((dice_num_list))
#
# dice_results()


    # from random import randint
    # repeat = True
    # while repeat:
    #     print(randint(1,10))
    #     print('roll again?: ')
    #     repeat = ('y' or 'yes') in input().lower()

#
#
#
# num_of type
#
# def dice_type(d_type):
#     query = input('what kind of die? (6, 10, or 20 sided)')
#     if query == '6':
#         from random import randint
#         repeat = True
#         while repeat:
#             print(randint(1,6) * (f'{ndie}'))
#             print('roll again?: ')
#             repeat = ('y' or 'yes') in input().lower()
#     elif query == '10':
#         from random import randint
#         repeat = True
#         while repeat:
#             print(randint(1,10))
#             print('roll again?: ')
#             repeat = ('y' or 'yes') in input().lower()
#     elif query == '20':
#         from random import randint
#         repeat = True
#         while repeat:
#             print(randint(1,20))
#             print('roll again?: ')
#             repeat = ('y' or 'yes') in input().lower()
