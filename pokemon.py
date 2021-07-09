
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
    def attack(self, name_attack, pokemon_d):
        for attack in self.attacks:
            if name_attack == attack:
                if attack.mode == pokemon_d.element:
                    result = pokemon_d.hp - attack.damage
                else:
                    if attack.mode == 'fire' and pokemon_d.element == 'grass':
                        result = pokemon_d.hp - (attack.damage * 1.5)
                        print(f'{self.name} has used {str(name_attack)}.\nThis attack has caused {attack.damage * 1.5} DP to {pokemon_d.name}, who has now {result} HP.')
                        pokemon_d.hp = result
                    elif attack.mode == 'fire' and pokemon_d.element == 'water':
                        result = pokemon_d.hp - (attack.damage * 0.5)
                        print(f'{self.name} has used {str(name_attack)}.\nThis attack has caused {attack.damage * 0.5} DP to {pokemon_d.name}, who has now {result} HP.')
                        pokemon_d.hp = result
                    elif attack.mode == 'grass' and pokemon_d.element == 'fire':
                        result = pokemon_d.hp - (attack.damage * 0.5)
                        print(f'{self.name} has used {str(name_attack)}.\nThis attack has caused {attack.damage * 0.5} DP to {pokemon_d.name}, who has now {result} HP.')
                        pokemon_d.hp = result
                    elif attack.mode == 'grass' and pokemon_d.element == 'water':
                        result = pokemon_d.hp - (attack.damage * 1.5)
                        print(f'{self.name} has used {str(name_attack)}.\nThis attack has caused {attack.damage * 1.5} DP to {pokemon_d.name}, who has now {result} HP.')
                        pokemon_d.hp = result
                    elif attack.mode == 'water' and pokemon_d.element == 'fire':
                        result = pokemon_d.hp - (attack.damage * 1.5)
                        print(f'{self.name} has used {str(name_attack)}.\nThis attack has caused {attack.damage * 1.5} DP to {pokemon_d.name}, who has now {result} HP.')
                        pokemon_d.hp = result
                    elif attack.mode == 'water' and pokemon_d.element == 'grass':
                        result = pokemon_d.hp - attack.damage
                        print(f'{self.name} has used {str(name_attack)}.\nThis attack has caused {attack.damage} DP to {pokemon_d.name}, who has now {result} HP.')
                        pokemon_d.hp = result
    def receive_dam(self, attack):
        if attack.element == self.element:
            self.hp -= attack.damage
        else:
            remain_elements = elements.copy()
            remain_elements = elements.remove(self.element)
            if attack.element == remain_elements[0]:
                self.hp -= attack.damage * 1.5
            else:
                self.hp -= attack.damage * 0.5
class Attack:
    def __init__(self, name, mode, damage):
        self.name = name
        self.mode = mode
        self.damage = damage
    def __repr__(self):
        return f'{self.name}'

charmander = Pokemon('Charmander', elements[0], 120)
bulbasaur = Pokemon('Bulbasaur', elements[1], 160)
squirtle = Pokemon('Squirtle', elements[2], 140)

flamethrower = Attack('Flamethrower', elements[0], 40)
razor_leaf = Attack('Razor Leaf', elements[1], 25)
surf = Attack('Surf', elements[2], 35)

charmander.learn(flamethrower)
bulbasaur.learn(razor_leaf)
squirtle.learn(surf)

pokemons = [charmander, bulbasaur, squirtle]

# for i, attack in enumerate(charmander.attacks):
#     print(f'{i + 1}. {attack}')

# user = int(input('Choose an attack: '))
# bulbasaur.receive_dam(charmander.attacks[user - 1])
# print(bulbasaur)

