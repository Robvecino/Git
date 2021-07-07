
elements = ['fire', 'grass', 'water']
class Pokemon:
    def __init__(self, name, element, hp):
        self.name = name
        self.element = element
        self.hp = hp
        self.attacks = []
    def __str__(self):
        return f'Name: {self.name}\nType: {self.element}\nHP: {self.hp}\nAttacks: {self.attacks}'
    def learn(self, attack):
        return self.attacks.append(attack)

class Attack:
    def __init__(self, name, mode, damage):
        self.name = name
        self.mode = mode
        self.damage = damage
    def __repr__(self):
        return f'Name: {self.name}'

charmander = Pokemon('Charmander', elements[0], 120)
bulbasaur = Pokemon('Bulbasaur', elements[1], 160)
squirtle = Pokemon('Squirtle', elements[2], 140)

print(charmander)
print(bulbasaur)
print(squirtle)

flamethrower = Attack('Flamethrower', elements[0], 40)
razor_leaf = Attack('Razor leaf', elements[1], 25)
surf = Attack('Surf', elements[2], 35)

charmander.learn(flamethrower)
print(charmander)
