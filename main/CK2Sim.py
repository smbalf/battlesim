import os
from army_choice import choose_units, army_one, army_two
from terrain_choice import choose_terrain
from sim_battle import simulate_battle

def run_battle(army_one, army_two, chosen_terrain):
    results = simulate_battle(army_one, army_two, chosen_terrain)

    if results['winner']:
        print(f'\n{results["winner"].upper()} WON THE BATTLE FOUGHT OVER {results["battle_round"]} ROUNDS!')
    else:
        print(f'\nTHE BATTLE WAS A DRAW FOUGHT OVER {results["battle_round"]} ROUNDS!')

    print(f"\nTerrain: {chosen_terrain} - Max possible rounds: {results['rounds']}")
    print(f"Start morale: {results['starting_morale_one']} v {results['starting_morale_two']}")
    print(f"End Morale: {results['army_one_morale']} v {results['army_two_morale']}")
    print(f"Start soldiers: {results['starting_soldiers_one']} v {results['starting_soldiers_two']}")
    print(f"End soldiers: {results['army_one_soldiers']} v {results['army_two_soldiers']}")

# RUNNING BATTLE SIMULATOR
os.system('cls')
army_one, army_two = choose_units(army_one, army_two)
chosen_terrain = choose_terrain()
run_battle(army_one, army_two, chosen_terrain)
