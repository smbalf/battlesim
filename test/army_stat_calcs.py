from terrain_file import terrain
from unit_file import unit_stats


def calc_unit_stats(unit_type, terrain_type, phase):
    stats = unit_stats[unit_type]
    terrain_modifiers = terrain[terrain_type][unit_type]
    # Calculate the modified attack and defence values
    if phase == "skirmish":
        attack = stats["attack_skirmish"] + terrain_modifiers["attack"]
        defence = stats["defence_skirmish"] + terrain_modifiers["defence"]
    elif phase == "melee":
        attack = stats["attack_melee"] + terrain_modifiers["attack"]
        defence = stats["defence_melee"] + terrain_modifiers["defence"]
    elif phase == "pursue":
        attack = stats["attack_pursue"] + terrain_modifiers["attack"]
        defence = stats["defence_pursue"] + terrain_modifiers["defence"]
    return attack, defence

def calc_army_stats(army, terrain, phase):
    # Initialize attack and defence values to 0
    attack = 0
    defence = 0
    # Calculate total attack and defence values for the army
    for unit, count in army.items():
        unit_attack, unit_defence = calc_unit_stats(unit, terrain, phase)
        attack += count * unit_attack
        defence += count * unit_defence
    return attack, defence