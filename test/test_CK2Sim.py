import os
from test_army_choice import choose_units, army_one, army_two
from test_terrain_choice import choose_terrain, terrain_list
from test_sim_battle import simulate_battle

def run_battle(army_one, army_two, chosen_terrain):
    for chosen_terrain in terrain_list:
        results = simulate_battle(army_one, army_two, chosen_terrain)

        if results['army_one_morale'] > results['army_two_morale']:
            print(f'ARMY ONE WON THE BATTLE! - {results["days"]} days')
        elif results['army_one_morale'] == results['army_two_morale']:
            print(f'THE BATTLE WAS A DRAW! - {results["days"]} days')
        else:
            print(f'ARMY TWO WON THE BATTLE! - {results["days"]} days')

        #print(f"\nStatistics of the battle fought on {chosen_terrain} over {results['days']} days:")
        print(f"Start morale: {results['starting_morale_one']} v {results['starting_morale_two']}")
        print(f"End Morale: {results['army_one_morale']} v {results['army_two_morale']}")
        print(f"Casualties: {results['army_one_casualties']} v {results['army_two_casualties']}")


# RUNNING BATTLE SIMULATOR
os.system('cls')

army_one, army_two = choose_units(army_one, army_two)

chosen_terrain = terrain_list #choose_terrain()

run_battle(army_one, army_two, chosen_terrain)
