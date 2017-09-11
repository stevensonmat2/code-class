class Weapons:
    def __init__(self, name, location, dmg, val, durability, ran_num):
        self.name = name
        self.location = location
        self.dmg = dmg
        self.val = val
        self.durability = durability
        self.ran_num = ran_num
    def __str__(self):
        return self.name
