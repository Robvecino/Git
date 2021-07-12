
elements = ['fire', 'grass', 'water']
class Pokemon:
    count = 0

    def set_count():
        Pokemon.count += 1
    def __init__(self, name, element, hp):
        self.name = name
        self.element = element
        self.hp = hp
        self.attacks = []
        self.is_alive = True
        self.xp = 10
        Pokemon.set_count()
    @property #TODO Este decorador hace que puedas acceder al método como una propiedad.
    def xp_damage(self):
        return self.xp * 0.1
    @property
    def stamina(self):
        return self.damage * self.xp
    def __str__(self):
        return f'Name: {self.name}\nType: {self.element}\nHP: {self.hp}\nAttacks: {self.attacks}'
    def learn(self, attack):
        return self.attacks.append(attack)
    def attack(self, name_attack, pokemon_d):
        for attack in self.attacks:
            if name_attack == attack:
                if attack.mode == pokemon_d.element:
                    result = pokemon_d.hp - attack.damage
                    pokemon_d.hp = result
                else:
                    if attack.mode == 'fire' and pokemon_d.element == 'grass':
                        result = pokemon_d.hp - (attack.damage * 1.5)
                        pokemon_d.hp = result
                        print(f'{self.name} has used {str(name_attack)}.\nThis attack has caused {attack.damage * 1.5} DP to {pokemon_d.name}, who has now {result} HP.')
                    elif attack.mode == 'fire' and pokemon_d.element == 'water':
                        result = pokemon_d.hp - (attack.damage * 0.5)
                        pokemon_d.hp = result
                        print(f'{self.name} has used {str(name_attack)}.\nThis attack has caused {attack.damage * 0.5} DP to {pokemon_d.name}, who has now {result} HP.')
                    elif attack.mode == 'grass' and pokemon_d.element == 'fire':
                        result = pokemon_d.hp - (attack.damage * 0.5)
                        pokemon_d.hp = result
                        print(f'{self.name} has used {str(name_attack)}.\nThis attack has caused {attack.damage * 0.5} DP to {pokemon_d.name}, who has now {result} HP.')
                    elif attack.mode == 'grass' and pokemon_d.element == 'water':
                        result = pokemon_d.hp - (attack.damage * 1.5)
                        pokemon_d.hp = result
                        print(f'{self.name} has used {str(name_attack)}.\nThis attack has caused {attack.damage * 1.5} DP to {pokemon_d.name}, who has now {result} HP.')
                    elif attack.mode == 'water' and pokemon_d.element == 'fire':
                        result = pokemon_d.hp - (attack.damage * 1.5)
                        pokemon_d.hp = result
                        print(f'{self.name} has used {str(name_attack)}.\nThis attack has caused {attack.damage * 1.5} DP to {pokemon_d.name}, who has now {result} HP.')
                    elif attack.mode == 'water' and pokemon_d.element == 'grass':
                        result = pokemon_d.hp - attack.damage
                        pokemon_d.hp = result
                        print(f'{self.name} has used {str(name_attack)}.\nThis attack has caused {attack.damage} DP to {pokemon_d.name}, who has now {result} HP.')
    def receive_dam(self, attack, damage_rate):
        if attack.element == self.element:
            self.hp -= attack.damage * damage_rate
            self.is_alive = True if self.hp > 0 else False
        else:
            remain_elements = elements.copy()
            remain_elements = elements.remove(self.element)
            if attack.element == remain_elements[0]:
                self.hp -= (attack.damage * damage_rate) * 1.5
                self.is_alive = True if self.hp > 0 else False

            else:
                self.hp -= (attack.damage * damage_rate)* 0.5
                self.is_alive = True if self.hp > 0 else False

class Attack:
    def __init__(self, name, mode, damage):
        self.name = name
        self.mode = mode
        self.damage = damage
    def __repr__(self):
        return f'"{self.name}"'

charmander = Pokemon('Charmander', elements[0], 120)
bulbasaur = Pokemon('Bulbasaur', elements[1], 160)
squirtle = Pokemon('Squirtle', elements[2], 140)

flamethrower = Attack('Flamethrower', elements[0], 40)
ember = Attack('Ember', elements[0], 9)
rage = Attack('Rage', elements[0], 20)
razor_leaf = Attack('Razor Leaf', elements[1], 25)
leech_seed = Attack('Leech Seed', elements[1], 10)
vine_wheep = Attack('Vine Wheep', elements[1], 15)
surf = Attack('Surf', elements[2], 35)
water_gun = Attack('Water Gun', elements[2], 25)
bubble = Attack('Burbuja', elements[2], 30)


charmander.learn(flamethrower)
charmander.learn(ember)
charmander.learn(rage)
bulbasaur.learn(razor_leaf)
bulbasaur.learn(leech_seed)
bulbasaur.learn(vine_wheep)
squirtle.learn(surf)
squirtle.learn(water_gun)
squirtle.learn(bubble)

pokemons = [charmander, bulbasaur, squirtle]

list_attaks_c = [flamethrower, ember, rage]
list_attaks_b = [razor_leaf, leech_seed, vine_wheep]
list_attaks_s = [surf, water_gun, bubble]

# for i, attack in enumerate(charmander.attacks):
#     print(f'{i + 1}. {attack}')

# user = int(input('Choose an attack: '))
# bulbasaur.receive_dam(charmander.attacks[user - 1])
# print(bulbasaur)

print(Pokemon.count)

