from pokemon import *
import random

print('POKEMON'.center(50, '-'))
print('Oak: Select your first pokemon...')
for i, pokemon in enumerate(pokemons):
    print(f'{i + 1}. {pokemon.name}')
user = int(input('Select a pokemon: ')) - 1
pokemon_a = pokemon[user]
print(random.choice(pokemons))
