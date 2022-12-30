import os
from unit_file import unit_stats
from army_stat_calcs import calc_army_stats
from damage_calcs import calc_damage


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
 
    army_one_panic = 0.35 * army_one_morale
    army_two_panic = 0.35 * army_two_morale

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

    battle_round = 0
    phase_switch = 4
    battle_phases = ['skirmish', 'melee', 'pursue']
    phase_type = 0
    while battle_round < rounds:
        battle_round += 1
        if phase_type == 0:
            phase = battle_phases[phase_type] # SKIRMISH
            army_one_attack, army_one_defence, army_two_attack, army_two_defence = calc_battle_stats()
        elif phase_type == 1:
            phase = battle_phases[phase_type] # MELEE
            army_one_attack, army_one_defence, army_two_attack, army_two_defence = calc_battle_stats()
        if battle_round % phase_switch == 0:
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

        army_one_soldiers, army_two_soldiers, army_one_morale, army_two_morale = calc_damage(battle_round, army_one, army_two, army_one_soldiers, army_two_soldiers, army_one_morale, army_two_morale, army_one_attack, army_two_attack, army_one_defence, army_two_defence, army_one_panic, army_two_panic)


        if army_one_soldiers < 0:
            army_one_soldiers = 0
            winner = 'army two'
            break
        elif army_one_morale < 0:
            winner = 'army two'
            break
        elif army_two_soldiers < 0:
            army_two_soldiers = 0
            winner = 'army one'
            break
        elif army_two_morale < 0:
            winner = 'army one'
            break
        else:
            winner = False
            break

    return {
        "winner": winner,
        "army_one_morale": round(army_one_morale, 0), 
        "army_two_morale": round(army_two_morale, 0),
        "rounds": rounds,
        "battle_round": battle_round,
        "starting_morale_one": starting_morale_one,
        "starting_morale_two": starting_morale_two,
        "starting_soldiers_one": starting_soldiers_one,
        "starting_soldiers_two": starting_soldiers_two,
        "army_one_soldiers": army_one_soldiers,
        "army_two_soldiers": army_two_soldiers
        }
