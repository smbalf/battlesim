import os
from test_unit_file import unit_stats
from test_army_stat_calcs import calc_army_stats


def simulate_battle(army_one, army_two, terrain):
    #os.system('cls')
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

    rounds = max(army_one_morale, army_two_morale)

    army_one_panic = 0.25 * army_one_morale
    army_two_panic = 0.25 * army_two_morale

    def battle():
        army_one_attack, army_one_defence = calc_army_stats(army_one, terrain, phase)
        army_two_attack, army_two_defence = calc_army_stats(army_two, terrain, phase)
        #print(f'ARMY ONE - Morale: {round(army_one_morale, 0)} | Attack: {round(army_one_attack, 0)} | Defence: {round(army_one_defence, 0)}')
        #print(f'ARMY TWO - Morale: {round(army_two_morale, 0)} | Attack: {round(army_two_attack, 0)} | Defence: {round(army_two_defence, 0)}')
        return army_one_attack, army_one_defence, army_two_attack, army_two_defence

    # BATTLE
    print(f'Maximum rounds: {rounds} - Terrain: {terrain}')
    day = 0
    while day < rounds:
        day += 1
        if army_one_morale < 0:
            break
        if army_two_morale < 0:
            break

        if day <= 4:
            phase = "skirmish"
            #print(f'\nDAY: {day} - Phase: {phase}')
            #print(f'Casualties: {army_one_casualties} - {army_two_casualties}')
            army_one_attack, army_one_defence, army_two_attack, army_two_defence = battle()
        elif day >= 5:
            if army_one_morale <= army_one_panic:
                phase = "pursue"
                #print(f'\nDAY: {day} - Phase: {phase}')
                #print(f'Casualties: {army_one_casualties} - {army_two_casualties}')
                army_one_attack, army_one_defence, army_two_attack, army_two_defence = battle()
            elif army_two_morale <= army_two_panic:
                phase = "pursue"
                #print(f'\nDAY: {day} - Phase: {phase}')
                #print(f'Casualties: {army_one_casualties} - {army_two_casualties}')
                army_one_attack, army_one_defence, army_two_attack, army_two_defence = battle()
            else:
                phase = "melee"
                #print(f'\nDAY: {day} - Phase: {phase}')
                #print(f'\nCasualties: {army_one_casualties} - {army_two_casualties}')
                army_one_attack, army_one_defence, army_two_attack, army_two_defence = battle()

        stat_factor = 10
        if day % 2 == 0:
            attack_army = army_one
            attack_stats = army_one_attack / stat_factor
            defence_army = army_two
            defence_stats = army_two_defence / stat_factor
        else:
            attack_army = army_two
            attack_stats = army_two_attack / stat_factor
            defence_army = army_one
            defence_stats = army_one_defence / stat_factor
        
        # Calculate damage dealt to defending army
        damage_dealt = attack_stats
        damage_taken = defence_stats
        
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
        army_one_casualties += round(damage_taken / army_one_units["morale"], 0)
        army_two_casualties += round(damage_dealt / army_two_units["morale"], 0)

        # Return the results of the battle
    return {
        "army_one_morale": round(army_one_morale, 0), 
        "army_two_morale": round(army_two_morale, 0),
        "army_one_casualties": round(army_one_casualties, 0),
        "army_two_casualties": round(army_two_casualties, 0), 
        "rounds": rounds,
        "days": day
        }
