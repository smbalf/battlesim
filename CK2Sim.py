import os
from army_choice import choose_units, army_one, army_two
from terrain_choice import choose_terrain
from sim_battle import simulate_battle

def run_battle(army_one, army_two, chosen_terrain):
    results = simulate_battle(army_one, army_two, chosen_terrain)

    if results['army_one_morale'] > results['army_two_morale']:
        print('\nARMY ONE WON THE BATTLE!')
    elif results['army_one_morale'] == results['army_two_morale']:
        print('\nTHE BATTLE WAS A DRAW!')
    else:
        print('\nARMY TWO WON THE BATTLE!')

    print(f"Final stats of the battle fought on {chosen_terrain} over {results['days']} days:")
    print(f"- Army One morale: {results['army_one_morale']}")
    print(f"- Army Two morale: {results['army_two_morale']}")
    print(f"- Army One casualties: {results['army_one_casualties']}")
    print(f"- Army Two casualties: {results['army_two_casualties']}")


# RUNNING BATTLE SIMULATOR
os.system('cls')
army_one, army_two = choose_units(army_one, army_two)
chosen_terrain = choose_terrain()
run_battle(army_one, army_two, chosen_terrain)
