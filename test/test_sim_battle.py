import os
from test_unit_file import unit_stats
from test_army_stat_calcs import calc_army_stats


def simulate_battle(army_one, army_two, terrain):
    army_one_morale = 0
    army_two_morale = 0
    army_one_soldiers = 0
    army_two_soldiers = 0

    for unit, count in army_one.items():
        army_one_units = unit_stats[unit]
        army_one_morale += army_one_units['morale'] * count
        army_one_soldiers += army_one_units['soldiers'] * count

    for unit, count in army_two.items():
        army_two_units = unit_stats[unit]
        army_two_morale += army_two_units['morale'] * count
        army_two_soldiers += army_two_units['soldiers'] * count
 
    army_one_panic = 0.25 * army_one_morale
    army_two_panic = 0.25 * army_two_morale

    starting_morale_one = army_one_morale
    starting_morale_two = army_two_morale
    starting_soldiers_one = army_one_soldiers
    starting_soldiers_two = army_two_soldiers

    def battle():
        army_one_attack, army_one_defence = calc_army_stats(army_one, terrain, phase)
        army_two_attack, army_two_defence = calc_army_stats(army_two, terrain, phase)
        return army_one_attack, army_one_defence, army_two_attack, army_two_defence

    # BATTLE
    rounds = max(army_one_morale, army_two_morale)
    
    day = 0
    while day < rounds:
        day += 1
        if day <= 4:
            phase = "skirmish"
            army_one_attack, army_one_defence, army_two_attack, army_two_defence = battle()
        elif day >= 5:
            if army_one_morale <= army_one_panic:
                phase = "pursue"
                army_one_attack, army_one_defence, army_two_attack, army_two_defence = battle()
            elif army_two_morale <= army_two_panic:
                phase = "pursue"
                army_one_attack, army_one_defence, army_two_attack, army_two_defence = battle()
            else:
                phase = "melee"
                army_one_attack, army_one_defence, army_two_attack, army_two_defence = battle()
        
        stat_factor = 2
        if day % 2 == 0:
            attack_army = army_one
            attack_stats = ((army_one_morale / 100) * (army_one_attack / stat_factor))
            defence_army = army_two
            defence_stats = ((army_two_morale / 100) * (army_two_defence / stat_factor))
        else:
            attack_army = army_two
            attack_stats = ((army_two_morale / 100) * (army_two_attack / stat_factor))
            defence_army = army_one
            defence_stats = ((army_one_morale / 100) * (army_one_defence / stat_factor))

        damage_dealt = round(attack_stats, 0)
        damage_taken = round(defence_stats, 0)
        morale_damage_dealt = damage_dealt / 10
        morale_damage_taken = damage_taken / 10

        if attack_army == army_one:
            army_two_morale -= morale_damage_dealt
            army_two_soldiers -= damage_dealt
        else: #if attack_army == army_two
            army_one_morale -= morale_damage_dealt
            army_one_soldiers -= damage_dealt

        if defence_army == army_one:
            army_one_morale -= morale_damage_taken
            army_one_soldiers -= damage_taken
        else: #if defence_army == army_two
            army_two_morale -= morale_damage_taken
            army_two_soldiers -= damage_taken

        if army_one_soldiers < 0:
            army_one_soldiers = 0
            break
        if army_two_soldiers <0:
            army_two_soldiers = 0
            break
        #print(f'{day}: dealt {damage_dealt} - taken {damage_taken} - mor_dealt{morale_damage_dealt}  mor_tak{morale_damage_taken}')

    return {
        "army_one_morale": round(army_one_morale, 0), 
        "army_two_morale": round(army_two_morale, 0),
        "rounds": rounds,
        "days": day,
        "starting_morale_one": starting_morale_one,
        "starting_morale_two": starting_morale_two,
        "starting_soldiers_one": starting_soldiers_one,
        "starting_soldiers_two": starting_soldiers_two,
        "army_one_soldiers": army_one_soldiers,
        "army_two_soldiers": army_two_soldiers
        }
