from pokemon import *
import random

print('POKEMON'.center(50, '-'))
print('Oak: Select your first pokemon...')
for i, pokemon in enumerate(pokemons):
    print(f'{i + 1}. {pokemon.name}')
user = int(input('Select a pokemon: ')) - 1
pokemon_a = pokemons[user]
oponent = (random.choice(pokemons))
print(f'This is your oponent: {oponent.name}')


while oponent.hp > 0:
    if pokemon_a == charmander:
        for i, attack in enumerate(list_attaks_c):
            print(f'{i + 1}. {attack.name}')
        user_attack = int(input('Select an attack: ')) - 1
        pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
        input('Continue to the next attack...')
    elif pokemon_a == bulbasaur:
        for i, attack in enumerate(list_attaks_b):
            print(f'{i + 1}. {attack.name}')
        user_attack = int(input('Select an attack: ')) - 1
        pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
        input('Continue to the next attack...')
    elif pokemon_a == squirtle:
        for i, attack in enumerate(list_attaks_s):
            print(f'{i + 1}. {attack.name}')
        user_attack = int(input('Select an attack: ')) - 1
        pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
        input('Continue to the next attack...')

