import os
from terrain_file import terrain, terrain_list
from unit_file import unit_stats, unit_list
from army_choice import choose_units, army_one, army_two
from terrain_choice import choose_terrain


def calc_unit_stats(unit_type, terrain_type):
    # Get the integer indices for the unit and terrain
    unit_index = unit_list.index(unit_type)
    terrain_index = terrain_list.index(terrain_type)

    # Use the integer indices to access the elements in the dictionaries
    stats = unit_stats[unit_type]
    print(terrain)
    print(terrain_index)
    print(unit_index)
    terrain_modifiers = terrain[terrain_index][unit_index]
    print(terrain_modifiers)
    print(stats)
    print(stats["attack_skirmish"])
    
    # Calculate the modified attack and defense values
    attack = stats["attack_skirmish"] * terrain_modifiers["attack"]
    defense = stats["defense_skirmish"] * terrain_modifiers["defense"]
    
    return attack, defense

def calc_army_stats(army, terrain):
    print("RUNNING CALC_ARMY_STATS")
    print(army)
    print(terrain)
    # Initialize attack and defense values to 0
    attack = 0
    defense = 0
    
    # Calculate total attack and defense values for the army
    for unit, count in army.items():
        unit_attack, unit_defense = calc_unit_stats(unit, terrain)
        attack += count * unit_attack
        defense += count * unit_defense
        """
        unit_stats = unit_stats[unit]
        attack += count * unit_stats["attack_melee"]
        defense += count * unit_stats["defense_melee"]
    
    # Modify attack and defense values based on terrain
    if terrain in terrain:
        for unit, count in army.items():
            terrain_modifiers = terrain[terrain][unit]
            attack += count * terrain_modifiers["attack"]
            defense += count * terrain_modifiers["defense"]
        """
    # Return modified attack and defense values
    return attack, defense

def simulate_battle(army_one, army_two, terrain):
    print("RUNNING SIMULATE_BATTLE")
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
    
    print(army_one_morale, army_two_morale)
    # Calculate attack and defense values for each army
    army_one_attack, army_one_defense = calc_army_stats(army_one, terrain)
    army_two_attack, army_two_defense = calc_army_stats(army_two, terrain)
    
    # Calculate number of rounds needed for battle
    rounds = max(army_one_morale, army_two_morale)

    for i in range(rounds):
        if i % 2 == 0:
            attack_army = army_one
            attack_stats = army_one_attack
            defense_army = army_two
            defense_stats = army_two_defense
        else:
            attack_army = army_two
            attack_stats = army_two_attack
            defense_army = army_one
            defense_stats = army_one_defense
        
        # Calculate damage dealt to defending army
        damage_dealt = sum([count * attack_stats[unit] for unit, count in attack_army.items()])
        damage_taken = sum([count * defense_stats[unit] for unit, count in defense_army.items()])
        
        # Reduce defending army's morale by damage dealt
        if attack_army == army_one:
            army_two_morale -= damage_dealt
        else:
            army_one_morale -= damage_dealt
        
        # Reduce attacking army's morale by damage taken
        if defense_army == army_one:
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
