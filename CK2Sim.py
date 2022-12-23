# Define the base stats for each unit type
unit_stats = {
    "archers": {
        "morale": 1,
        "maintenance": 2,
        "attack_skirmish": 2,
        "attack_melee": 1,
        "attack_pursue": 2,
        "defense_skirmish": 1.5,
        "defense_melee": 1.5,
        "defense_pursue": 2.25
    },
    "light_inf": {
        "morale": 2,
        "maintenance": 0.7,
        "attack_skirmish": 1.25,
        "attack_melee": 1,
        "attack_pursue": 2,
        "defense_skirmish": 2,
        "defense_melee": 1,
        "defense_pursue": 2.5
    },
    "pikemen": {
        "morale": 6,
        "maintenance": 2.5,
        "attack_skirmish": 0.1,
        "attack_melee": 4.5,
        "attack_pursue": 0.2,
        "defense_skirmish": 4,
        "defense_melee": 4.5,
        "defense_pursue": 2
    },
    "heavy_inf": {
        "morale": 4,
        "maintenance": 3,
        "attack_skirmish": 0.25,
        "attack_melee": 6,
        "attack_pursue": 1,
        "defense_skirmish": 3,
        "defense_melee": 4,
        "defense_pursue": 4
    },
    "light_cav": {
        "morale": 4,
        "maintenance": 3,
        "attack_skirmish": 2,
        "attack_melee": 3,
        "attack_pursue": 6,
        "defense_skirmish": 4.5,
        "defense_melee": 3,
        "defense_pursue": 4.5
    },
    "heavy_cav": {
        "morale": 10,
        "maintenance": 6,
        "attack_skirmish": 0.5,
        "attack_melee": 10,
        "attack_pursue": 4,
        "defense_skirmish": 6,
        "defense_melee": 6,
        "defense_pursue": 5
    },
    "horse_archers": {
        "morale": 3,
        "maintenance": 4,
        "attack_skirmish": 4,
        "attack_melee": 3,
        "attack_pursue": 7,
        "defense_skirmish": 4,
        "defense_melee": 4,
        "defense_pursue": 5
    },
        "war_ele": {
        "morale": 15,
        "maintenance": 20,
        "attack_skirmish": 0.25,
        "attack_melee": 25,
        "attack_pursue": 0.25,
        "defense_skirmish": 5,
        "defense_melee": 15,
        "defense_pursue": 2
    },
    "camel_cav": {
        "morale": 5,
        "maintenance": 3,
        "attack_skirmish": 4,
        "attack_melee": 6,
        "attack_pursue": 4,
        "defense_skirmish": 4.5,
        "defense_melee": 3,
        "defense_pursue": 2.5
    }
}

terrain = {
    "hill": {
        "archers": {
            "attack": 0.2,
            "defense": 0.5
        },
        "light_inf": {
            "attack": 0,
            "defense": 0.3
        },
        "pikemen": {
            "attack": 0.1,
            "defense": 0.2
        },
        "heavy_inf": {
            "attack": 0,
            "defense": 0.2
        },
        "light_cav": {
            "attack": 0,
            "defense": 0.15
        },
        "heavy_cav": {
            "attack": 0,
            "defense": 0
        },
        "horse_archers": {
            "attack": 0.1,
            "defense": 0.15
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
    "mountain": {
        "archers": {
            "attack": 0.5,
            "defense": 1
        },
        "light_inf": {
            "attack": 0,
            "defense": 1
        },
        "pikemen": {
            "attack": 0,
            "defense": 0.5
        },
        "heavy_inf": {
            "attack": 0,
            "defense": 0.5
        },
        "light_cav": {
            "attack": 0,
            "defense": 0
        },
        "heavy_cav": {
            "attack": 0,
            "defense": 0
        },
        "horse_archers": {
            "attack": 0,
            "defense": 0
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
    "stream": {
        "archers": {
            "attack": -0.1,
            "defense": -0.2
        },
        "light_inf": {
            "attack": -0.1,
            "defense": -0.2
        },
        "pikemen": {
            "attack": -0.15,
            "defense": -0.3
        },
        "heavy_inf": {
            "attack": -0.15,
            "defense": -0.3
        },
        "light_cav": {
            "attack": -0.2,
            "defense": -0.2
        },
        "heavy_cav": {
            "attack": -0.3,
            "defense": -0.3
        },
        "horse_archers": {
            "attack": -0.2,
            "defense": -0.2
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
       "forest": {
        "archers": {
            "attack": 0,
            "defense": 0.3
        },
        "light_inf": {
            "attack": 0.5,
            "defense": 0.3
        },
        "pikemen": {
            "attack": 0.1,
            "defense": 0.1
        },
        "heavy_inf": {
            "attack": 0,
            "defense": 0.1
        },
        "light_cav": {
            "attack": 0,
            "defense": 0.15
        },
        "heavy_cav": {
            "attack": 0,
            "defense": 0
        },
        "horse_archers": {
            "attack": 0.15,
            "defense": 0.15
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
    "desert": {
        "archers": {
            "attack": -0.05,
            "defense": -0.1
        },
        "light_inf": {
            "attack": -0.1,
            "defense": -0.1
        },
        "pikemen": {
            "attack": -0.15,
            "defense": -0.15
        },
        "heavy_inf": {
            "attack": -0.15,
            "defense": -0.15
        },
        "light_cav": {
            "attack": -0.125,
            "defense": -0.125
        },
        "heavy_cav": {
            "attack": -0.15,
            "defense": -0.15
        },
        "horse_archers": {
            "attack": -0.075,
            "defense": -0.125
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0.5,
            "defense": 0.5
        }
    },
    "stream": {
        "archers": {
            "attack": -0.1,
            "defense": -0.2
        },
        "light_inf": {
            "attack": -0.1,
            "defense": -0.2
        },
        "pikemen": {
            "attack": -0.15,
            "defense": -0.3
        },
        "heavy_inf": {
            "attack": -0.15,
            "defense": -0.3
        },
        "light_cav": {
            "attack": -0.2,
            "defense": -0.2
        },
        "heavy_cav": {
            "attack": -0.3,
            "defense": -0.3
        },
        "horse_archers": {
            "attack": -0.2,
            "defense": -0.2
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
        "river": {
        "archers": {
            "attack": -0.1,
            "defense": -0.15
        },
        "light_inf": {
            "attack": -0.15,
            "defense": -0.15
        },
        "pikemen": {
            "attack": -0.3,
            "defense": -0.3
        },
        "heavy_inf": {
            "attack": -0.3,
            "defense": -0.3
        },
        "light_cav": {
            "attack": -0.2,
            "defense": -0.2
        },
        "heavy_cav": {
            "attack": -0.3,
            "defense": -0.3
        },
        "horse_archers": {
            "attack": -0.2,
            "defense": -0.2
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
    "strait": {
        "archers": {
            "attack": -0.1,
            "defense": -0.15
        },
        "light_inf": {
            "attack": -0.15,
            "defense": -0.15
        },
        "pikemen": {
            "attack": -0.2,
            "defense": -0.2
        },
        "heavy_inf": {
            "attack": -0.2,
            "defense": -0.2
        },
        "light_cav": {
            "attack": -0.175,
            "defense": -0.175
        },
        "heavy_cav": {
            "attack": -0.2,
            "defense": -0.2
        },
        "horse_archers": {
            "attack": -0.125,
            "defense": -0.175
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
    "amphibious": {
        "archers": {
            "attack": -0.1,
            "defense": -0.15
        },
        "light_inf": {
            "attack": -0.15,
            "defense": -0.15
        },
        "pikemen": {
            "attack": -0.2,
            "defense": -0.2
        },
        "heavy_inf": {
            "attack": -0.2,
            "defense": -0.2
        },
        "light_cav": {
            "attack": -0.2,
            "defense": -0.2
        },
        "heavy_cav": {
            "attack": -0.3,
            "defense": -0.3
        },
        "horse_archers": {
            "attack": -0.2,
            "defense": -0.2
        },
        "war_ele": {
            "attack": -0.15,
            "defense": -0.2
        },
        "camel_cav": {
            "attack": -0.2,
            "defense": -0.2
        }
    }
}

unit_list = []
terrain_list = []

for key in terrain.keys():
    terrain_list.append(key)

for key in unit_stats.keys():
    unit_list.append(key)

army_one = {}
army_two = {}

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



def choose_units(army_one, army_two):
    gold_one = 100
    gold_two = 100

    # Choose units for army one
    print("Army one, choose your units:")
    i = 0
    for unit, stats in unit_stats.items():
        print(f"{i}: {unit} (maintenance cost: {stats['maintenance']})")
        i += 1

    while gold_one > 0:
        try:
            choice = input("Enter the number of the unit you want to add to your army (or 'done' when finished): ")
            if choice == "done":
                break
            elif int(choice) in range(len(unit_stats)):
                unit = list(unit_stats.keys())[int(choice)]
                cost = unit_stats[unit]["maintenance"]
                if gold_one - cost >= 0:
                    gold_one -= cost
                    army_one[unit] = 0
                    print(f"Added {unit} to army one for {cost} gold. {gold_one} gold remaining.")
                else:
                    print("Not enough gold. Please choose a different unit or type 'done' to finish.")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please try again.")

    # Choose units for army two
    print("\nArmy two, choose your units:")
    i = 0
    for unit, stats in unit_stats.items():
        print(f"{i}: {unit} (maintenance cost: {stats['maintenance']})")
        i += 1

    while gold_two > 0:
        try:
            choice = input("Enter the number of the unit you want to add to your army (or 'done' when finished): ")
            if choice == "done":
                break
            elif int(choice) in range(len(unit_stats)):
                unit = list(unit_stats.keys())[int(choice)]
                cost = unit_stats[unit]["maintenance"]
                if gold_two - cost >= 0:
                    gold_two -= cost
                    army_two[unit] = 0
                    print(f"Added {unit} to army two for {cost} gold. {gold_two} gold remaining.")
                else:
                    print("Not enough gold. Please choose a different unit or type 'done' to finish.")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please try again.")
            
    return army_one, army_two


def calc_army_stats(army, terrain):
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
    global unit_stats
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

def run_battle(army_one, army_two):
    global terrain
    # Display list of terrain options to player
    print("Choose the terrain for the battle:")
    for i, terrain in enumerate(terrain.keys()):
        print(f"{i}: {terrain}")
    # Prompt player to choose terrain
    terrain_choice = input("Enter the number of the terrain you want to use: ")
    terrain_choice = int(terrain_choice)
    chosen_terrain = terrain_list[terrain_choice]

    # Simulate the battle
    results = simulate_battle(army_one, army_two, chosen_terrain)

    # Display results of the battle
    print("Results of the battle:")
    print(f"Army one morale: {results['army_one_morale']}")
    print(f"Army two morale: {results['army_two_morale']}")
    print(f"Army one casualties: {results['army_one_casualties']}")
    print(f"Army two casualties: {results['army_two_casualties']}")




import os

os.system('cls')

print("ARMY BATTLE SIMULATOR")
army_one, army_two = choose_units(army_one, army_two)

run_battle(army_one, army_two)
