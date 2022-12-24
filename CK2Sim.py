import os
from terrain_file import terrain, terrain_list
from unit_file import unit_stats, unit_list
from army_choice import choose_units, army_one, army_two
from terrain_choice import choose_terrain
from army_stat_calcs import calc_army_stats, calc_unit_stats


def simulate_battle(army_one, army_two, terrain):
    os.system('cls')
    print("RUNNING SIMULATE_BATTLE\n")
    # Initialize variables to keep track of battle stats
    army_one_morale = 0
    army_two_morale = 0
    army_one_casualties = 0
    army_two_casualties = 0
    
    # Calculate total morale for each army
    for unit, count in army_one.items():
        army_one_units = unit_stats[unit]
        army_one_morale += army_one_units["morale"] * count
    for unit, count in army_two.items():
        army_two_units = unit_stats[unit]
        army_two_morale += army_two_units["morale"] * count

    # Calculate attack and defence values for each army
    army_one_attack, army_one_defence = calc_army_stats(army_one, terrain)
    army_two_attack, army_two_defence = calc_army_stats(army_two, terrain)
    print(f'ARMY ONE - Morale: {army_one_morale} | Attack: {army_one_attack} | Defence: {army_one_defence}')
    print(f'ARMY TWO - Morale: {army_two_morale} | Attack: {army_two_attack} | Defence: {army_two_defence}')

    # Calculate number of rounds needed for battle
    rounds = max(army_one_morale, army_two_morale)
    print(f'Rounds: {rounds}')

    for i in range(rounds):
        if i % 2 == 0:
            attack_army = army_one
            attack_stats = army_one_attack
            defence_army = army_two
            defence_stats = army_two_defence
        else:
            attack_army = army_two
            attack_stats = army_two_attack
            defence_army = army_one
            defence_stats = army_one_defence
        
        # Calculate damage dealt to defending army
        for unit, count in attack_army.items():
            print(attack_stats[unit])
            print(count)
        damage_dealt = sum([count * attack_stats[unit] for unit, count in attack_army.items()])
        damage_taken = sum([count * defence_stats[unit] for unit, count in defence_army.items()])
        
        # Reduce defending army's morale by damage dealt
        if attack_army == army_one:
            army_two_morale -= damage_dealt
        else:
            army_one_morale -= damage_dealt
        
        # Reduce attacking army's morale by damage taken
        if defence_army == army_one:
            army_one_morale -= damage_taken
        else:
            army_two_morale -= damage_taken
        
        # Calculate casualties for each army
        army_one_casualties += damage_taken / army_one_units["morale"]
        army_two_casualties += damage_dealt / army_two_units["morale"]

    # Return the results of the battle
    return {"army_one_morale": army_one_morale, "army_two_morale": army_two_morale,
            "army_one_casualties": army_one_casualties, "army_two_casualties": army_two_casualties}

def run_battle(army_one, army_two, chosen_terrain):
    results = simulate_battle(army_one, army_two, chosen_terrain)

    # Display results of the battle
    print("Results of the battle:")
    print(f"Army one morale: {results['army_one_morale']}")
    print(f"Army two morale: {results['army_two_morale']}")
    print(f"Army one casualties: {results['army_one_casualties']}")
    print(f"Army two casualties: {results['army_two_casualties']}")


# The simulator
os.system('cls')

army_one, army_two = choose_units(army_one, army_two)

chosen_terrain = choose_terrain()

run_battle(army_one, army_two, chosen_terrain)
