import os
from test_unit_file import unit_stats
from test_army_stat_calcs import calc_army_stats
from test_damage_calcs import calc_damage


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

    def calc_battle_stats():
        army_one_attack, army_one_defence = calc_army_stats(army_one, terrain, phase)
        army_two_attack, army_two_defence = calc_army_stats(army_two, terrain, phase)
        return army_one_attack, army_one_defence, army_two_attack, army_two_defence

    # BATTLE
    rounds = max(army_one_morale, army_two_morale)

    day = 0
    phase_switch = 3
    battle_phases = ['skirmish', 'melee', 'pursue']
    phase_type = 0
    while day < rounds:
        day += 1
        if day % phase_switch == 0:
            if phase_type == 0:
                phase_type += 1
                phase = battle_phases[phase_type] # SKIRMISH
                army_one_attack, army_one_defence, army_two_attack, army_two_defence = calc_battle_stats()
            elif phase_type == 1:
                phase_type -= 1
                phase = battle_phases[phase_type] # MELEE
                army_one_attack, army_one_defence, army_two_attack, army_two_defence = calc_battle_stats()
        if army_one_morale <= army_one_panic:
            phase = battle_phases[2] # PURSUE
            army_one_attack, army_one_defence, army_two_attack, army_two_defence = calc_battle_stats()
        elif army_two_morale <= army_two_panic:
            phase = battle_phases[2] # PURSUE
            army_one_attack, army_one_defence, army_two_attack, army_two_defence = calc_battle_stats()
        



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
