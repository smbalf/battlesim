import os
from test_army_choice import choose_units, army_one, army_two
from test_terrain_choice import choose_terrain, terrain_list
from test_sim_battle import simulate_battle

def run_battle(army_one, army_two, chosen_terrain):
    for chosen_terrain in terrain_list:
        results = simulate_battle(army_one, army_two, chosen_terrain)

        if results['army_one_morale'] > results['army_two_morale']:
            print('ARMY ONE WON THE BATTLE!')
        elif results['army_one_morale'] == results['army_two_morale']:
            print('THE BATTLE WAS A DRAW!')
        else:
            print('ARMY TWO WON THE BATTLE!')

        #print(f"\nStatistics of the battle fought on {chosen_terrain} over {results['days']} days:")
        print(f"Morale: {results['army_one_morale']} v {results['army_two_morale']}")
        print(f"Casualties: {results['army_one_casualties']} v {results['army_two_casualties']}")


# RUNNING BATTLE SIMULATOR
os.system('cls')

army_one, army_two = choose_units(army_one, army_two)

chosen_terrain = terrain_list #choose_terrain()

run_battle(army_one, army_two, chosen_terrain)
