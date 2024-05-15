import requests
# EXO 1

import requests
pikachu_data = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu');
 
print(pikachu_data)
 
print(pikachu_data.json()['name']);


# EXO 2 diff entre pokemon


def combat(pokemon1, pokemon2):

    pokemon1_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon1}').json()
    pokemon2_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon2}').json()
    

    pokemon1_id = pokemon1_data['id']
    pokemon2_id = pokemon2_data['id']
    

    if pokemon1_id < pokemon2_id:
        print(f"L'ID de {pokemon1.capitalize()} ({pokemon1_id}) est inférieur à l'ID de {pokemon2.capitalize()} ({pokemon2_id}).")
    elif pokemon1_id > pokemon2_id:
        print(f"L'ID de {pokemon1.capitalize()} ({pokemon1_id}) est supérieur à l'ID de {pokemon2.capitalize()} ({pokemon2_id}).")
   


combat('pikachu', 'charmeleon')

    
    