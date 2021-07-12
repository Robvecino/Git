from pokemon import *
import random

def battle(db, pokemon_a, oponent):
    first_attack = random.choice(db)
    if first_attack == pokemon_a:
        print('You begin first')
        while pokemon_a.hp > 0 and oponent.hp > 0:
            if pokemon_a == charmander:
                for i, attack in enumerate(list_attaks_c):
                    print(f'{i + 1}. {attack.name}')
                user_attack = int(input('Select an attack: ')) - 1
                pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
                input('Now is the turn of the oponent')
                if oponent.hp > 0:
                    if oponent == charmander:
                        oponent_choice = random.choice(list_attaks_c)
                        oponent.attack(oponent_choice, pokemon_a)
                        input('Now is your turn')
                    elif oponent == bulbasaur:
                        oponent_choice = random.choice(list_attaks_b)
                        oponent.attack(oponent_choice, pokemon_a)
                        input('Now is your turn')
                    elif oponent == squirtle:
                        oponent_choice = random.choice(list_attaks_s)
                        oponent.attack(oponent_choice, pokemon_a)
                        input('Now is your turn')
            elif pokemon_a == bulbasaur:
                for i, attack in enumerate(list_attaks_b):
                    print(f'{i + 1}. {attack.name}')
                user_attack = int(input('Select an attack: ')) - 1
                pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
                input('Now is the turn of the oponent')
                if oponent.hp > 0:
                    if oponent == charmander:
                        oponent_choice = random.choice(list_attaks_c)
                        oponent.attack(oponent_choice, pokemon_a)
                        input('Now is your turn')
                    elif oponent == bulbasaur:
                        oponent_choice = random.choice(list_attaks_b)
                        oponent.attack(oponent_choice, pokemon_a)
                        input('Now is your turn')
                    elif oponent == squirtle:
                        oponent_choice = random.choice(list_attaks_s)
                        oponent.attack(oponent_choice, pokemon_a)
                        input('Now is your turn')
            elif pokemon_a == squirtle:
                for i, attack in enumerate(list_attaks_s):
                    print(f'{i + 1}. {attack.name}')
                user_attack = int(input('Select an attack: ')) - 1
                pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
                input('Now is the turn of the oponent')
                if oponent.hp > 0:
                    if oponent == charmander:
                        oponent_choice = random.choice(list_attaks_c)
                        oponent.attack(oponent_choice, pokemon_a)
                        input('Now is your turn')
                    elif oponent == bulbasaur:
                        oponent_choice = random.choice(list_attaks_b)
                        oponent.attack(oponent_choice, pokemon_a)
                        input('Now is your turn')
                    elif oponent == squirtle:
                        oponent_choice = random.choice(list_attaks_s)
                        oponent.attack(oponent_choice, pokemon_a)
                        input('Now is your turn')
    else:
        print('Your oponent begins first')
        while pokemon_a.hp > 0 and oponent.hp > 0:
            if oponent == charmander:
                oponent_choice = random.choice(list_attaks_c)
                oponent.attack(oponent_choice, pokemon_a)
                input('Now is your turn')
                if pokemon_a.hp > 0:
                    if pokemon_a == charmander:
                        for i, attack in enumerate(list_attaks_c):
                            print(f'{i + 1}. {attack.name}')
                        user_attack = int(input('Select an attack: ')) - 1
                        pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
                        input('Now is the turn of the oponent')
                    elif pokemon_a == bulbasaur:
                        for i, attack in enumerate(list_attaks_b):
                            print(f'{i + 1}. {attack.name}')
                        user_attack = int(input('Select an attack: ')) - 1
                        pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
                        input('Now is the turn of the oponent')
                    elif pokemon_a == squirtle:
                        for i, attack in enumerate(list_attaks_s):
                            print(f'{i + 1}. {attack.name}')
                        user_attack = int(input('Select an attack: ')) - 1
                        pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
                        input('Now is the turn of the oponent')
            elif oponent == bulbasaur:
                oponent_choice = random.choice(list_attaks_b)
                oponent.attack(oponent_choice, pokemon_a)
                input('Now is your turn')
                if pokemon_a.hp > 0:
                    if pokemon_a == charmander:
                        for i, attack in enumerate(list_attaks_c):
                            print(f'{i + 1}. {attack.name}')
                        user_attack = int(input('Select an attack: ')) - 1
                        pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
                        input('Now is the turn of the oponent')
                    elif pokemon_a == bulbasaur:
                        for i, attack in enumerate(list_attaks_b):
                            print(f'{i + 1}. {attack.name}')
                        user_attack = int(input('Select an attack: ')) - 1
                        pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
                        input('Now is the turn of the oponent')
                    elif pokemon_a == squirtle:
                        for i, attack in enumerate(list_attaks_s):
                            print(f'{i + 1}. {attack.name}')
                        user_attack = int(input('Select an attack: ')) - 1
                        pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
                        input('Now is the turn of the oponent')
            elif oponent == squirtle:
                oponent_choice = random.choice(list_attaks_s)
                oponent.attack(oponent_choice, pokemon_a)
                input('Now is your turn')
                if pokemon_a.hp > 0:
                    if pokemon_a == charmander:
                        for i, attack in enumerate(list_attaks_c):
                            print(f'{i + 1}. {attack.name}')
                        user_attack = int(input('Select an attack: ')) - 1
                        pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
                        input('Now is the turn of the oponent')
                    elif pokemon_a == bulbasaur:
                        for i, attack in enumerate(list_attaks_b):
                            print(f'{i + 1}. {attack.name}')
                        user_attack = int(input('Select an attack: ')) - 1
                        pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
                        input('Now is the turn of the oponent')
                    elif pokemon_a == squirtle:
                        for i, attack in enumerate(list_attaks_s):
                            print(f'{i + 1}. {attack.name}')
                        user_attack = int(input('Select an attack: ')) - 1
                        pokemon_a.attack(pokemon_a.attacks[user_attack], oponent)
                    input('Now is the turn of the oponent')
    if pokemon_a.hp <= 0:
        print('You was defeated.\nYou lose.')
    elif oponent.hp <= 0:
        print('The oponent was defeated.\nYou win.')