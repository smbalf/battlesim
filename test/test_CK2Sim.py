import os
from army_choice import choose_units, army_one, army_two
from terrain_choice import choose_terrain, terrain_list
from sim_battle import simulate_battle

def run_battle(army_one, army_two, chosen_terrain):
    for chosen_terrain in terrain_list:
        results = simulate_battle(army_one, army_two, chosen_terrain)

        if results['army_one_morale'] > results['army_two_morale']:
            print('ARMY ONE WON THE BATTLE!\n')
        elif results['army_one_morale'] == results['army_two_morale']:
            print('THE BATTLE WAS A DRAW!\n')
        else:
            print('ARMY TWO WON THE BATTLE!\n')

        #print(f"\nStatistics of the battle fought on {chosen_terrain} over {results['days']} days:")
        print(f"Army One morale: {results['army_one_morale']}")
        print(f"Army Two morale: {results['army_two_morale']}")
        print(f"Army One casualties: {results['army_one_casualties']}")
        print(f"Army Two casualties: {results['army_two_casualties']}")


# RUNNING BATTLE SIMULATOR
os.system('cls')

army_one, army_two = choose_units(army_one, army_two)

chosen_terrain = terrain_list #choose_terrain()

run_battle(army_one, army_two, chosen_terrain)

"""

"""