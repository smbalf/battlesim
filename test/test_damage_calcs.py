
def calc_damage(day, army_one, army_two, 
                army_one_soldiers, army_two_soldiers,
                army_one_morale, army_two_morale, 
                army_one_attack, army_two_attack,
                army_one_defence, army_two_defence):
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
    if army_two_soldiers < 0:
        army_two_soldiers = 0

    return attack_army, defence_army, damage_dealt, damage_taken, morale_damage_dealt, morale_damage_taken
