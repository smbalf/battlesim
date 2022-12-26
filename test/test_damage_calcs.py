
def calc_damage(day, army_one, army_two, 
                army_one_soldiers, army_two_soldiers,
                army_one_morale, army_two_morale, 
                army_one_attack, army_two_attack,
                army_one_defence, army_two_defence):
    stat_factor = 2
    if day % 2 == 0:
        attack_army = army_one
        attack_stats = 0
        defence_army = army_two
        defence_stats = 0
    else:
        attack_army = army_two
        attack_stats = 0
        defence_army = army_one
        defence_stats = 0

    damage_dealt = 0
    damage_taken = 0
    morale_damage_dealt = 0
    morale_damage_taken = 0
    
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
    if army_two_soldiers < 0:
        army_two_soldiers = 0

    return attack_army, defence_army, damage_dealt, damage_taken, morale_damage_dealt, morale_damage_taken
