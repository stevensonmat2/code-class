# class NPC:
#     def __init__(self, name):
#         self.weapon = weapon('club', 5)
#         self.name = name
#         self.hp = 100
#
#
#
#
# class weapon:
#     def __init__(self, name, ap):
#         self.name = name
#         self.ap = ap
#
#     def __str__(self):
#         return self.name
#
#
# def round_of_battle(NPC1, NPC2):
#     NPC1.hp -= NPC2.weapon.ap
#     NPC2.hp -= NPC1.weapon.ap
#
#
#
#
#
# player = NPC('Chris')
#
#
# orc = NPC('Orc Guy')
# sword = weapon('sword of ouch', 20)
# axe = weapon('Axe', 20)
#
# player.weapon = sword
# orc.weapon = axe
#
# print(player.weapon)



# class Foo:
#     def __init__(self, name):
#         self.name = name
#
#
#
# lst = []
#
# for i in range(100):
#     lst.append(Foo(i))
#
# for x in lst:
#     print(x.name)



lst = []

for i in range(1, 21):
    lst.append(i)

print(lst)

lst2 = [i for i in range(1, 21)]

print(lst2)













