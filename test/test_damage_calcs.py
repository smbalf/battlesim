
def calc_damage(day, army_one, army_two, 
                army_one_soldiers, army_two_soldiers,
                army_one_morale, army_two_morale, 
                army_one_attack, army_two_attack,
                army_one_defence, army_two_defence, army_one_panic, army_two_panic):

    if army_one_morale <= army_one_panic:
        army_one_attack /= 3
        army_one_defence /= 6
    if 0 < army_one_morale <= (army_one_panic/2):
        army_one_attack /= 5
        army_one_defence /= 8 
        #print('army one hell')
    if army_two_morale <= army_two_panic:
        army_two_attack /= 3
        army_two_defence /= 6
    if 0 < army_two_morale <= (army_two_panic/2):
        army_two_attack /= 5
        army_two_defence /= 8 
        #print('army two hell')

    if day % 2 == 0:
        attack_army = army_one
        attacker_att_stats = army_one_attack
        attacker_def_stats = army_one_defence
        #print(attacker_att_stats, attacker_def_stats)
        defence_army = army_two
        defender_att_stats = army_two_defence
        defender_def_stats = army_two_defence
    else:
        attack_army = army_two
        attacker_att_stats = army_two_attack
        attacker_def_stats = army_two_defence
        defence_army = army_one
        defender_att_stats = army_one_attack
        defender_def_stats = army_one_defence
        #print(defender_att_stats, defender_def_stats)
    
    damage_dealt = round((attacker_att_stats / defender_def_stats) * 4 , 0)
    damage_taken = round((defender_att_stats / attacker_def_stats) * 4, 0)
    morale_damage_dealt = round((attacker_att_stats / defender_def_stats) / 2 , 0)
    morale_damage_taken = round((defender_att_stats / attacker_def_stats) / 2, 0)
    #print(day)
    #print(attack_army, "dmg",  damage_dealt, damage_taken, "stats", attacker_att_stats, attacker_def_stats)
    #print(defence_army, "dmg", damage_dealt, damage_taken, "stats", defender_att_stats, defender_def_stats)
    
    if attack_army == army_one:
        army_one_morale -= morale_damage_taken
        army_one_soldiers -= damage_taken
        army_two_morale -= morale_damage_dealt
        army_two_soldiers -= damage_dealt
    else: #if attack_army == army_two
        army_one_morale -= morale_damage_dealt
        army_one_soldiers -= damage_dealt
        army_two_morale -= morale_damage_taken
        army_two_soldiers -= damage_taken

    return army_one_soldiers, army_two_soldiers, army_one_morale, army_two_morale, damage_taken, damage_dealt, morale_damage_dealt, morale_damage_taken
