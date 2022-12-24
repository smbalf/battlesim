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

unit_list = []

for key in unit_stats.keys():
    unit_list.append(key)