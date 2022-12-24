unit_stats = {
    "archers": {
        "morale": 1,
        "maintenance": 2,
        "attack_skirmish": 2,
        "attack_melee": 1,
        "attack_pursue": 2,
        "defence_skirmish": 1.5,
        "defence_melee": 1.5,
        "defence_pursue": 2.25
    },
    "light_inf": {
        "morale": 2,
        "maintenance": 0.7,
        "attack_skirmish": 1.25,
        "attack_melee": 1,
        "attack_pursue": 2,
        "defence_skirmish": 2,
        "defence_melee": 1,
        "defence_pursue": 2.5
    },
    "pikemen": {
        "morale": 6,
        "maintenance": 2.5,
        "attack_skirmish": 0.1,
        "attack_melee": 4.5,
        "attack_pursue": 0.2,
        "defence_skirmish": 4,
        "defence_melee": 4.5,
        "defence_pursue": 2
    },
    "heavy_inf": {
        "morale": 4,
        "maintenance": 3,
        "attack_skirmish": 0.25,
        "attack_melee": 6,
        "attack_pursue": 1,
        "defence_skirmish": 3,
        "defence_melee": 4,
        "defence_pursue": 4
    },
    "light_cav": {
        "morale": 4,
        "maintenance": 3,
        "attack_skirmish": 2,
        "attack_melee": 3,
        "attack_pursue": 6,
        "defence_skirmish": 4.5,
        "defence_melee": 3,
        "defence_pursue": 4.5
    },
    "heavy_cav": {
        "morale": 10,
        "maintenance": 6,
        "attack_skirmish": 0.5,
        "attack_melee": 10,
        "attack_pursue": 4,
        "defence_skirmish": 6,
        "defence_melee": 6,
        "defence_pursue": 5
    },
    "horse_archers": {
        "morale": 3,
        "maintenance": 4,
        "attack_skirmish": 4,
        "attack_melee": 3,
        "attack_pursue": 7,
        "defence_skirmish": 4,
        "defence_melee": 4,
        "defence_pursue": 5
    },
    "war_ele": {
        "morale": 15,
        "maintenance": 20,
        "attack_skirmish": 0.25,
        "attack_melee": 25,
        "attack_pursue": 0.25,
        "defence_skirmish": 5,
        "defence_melee": 15,
        "defence_pursue": 2
    },
    "camel_cav": {
        "morale": 5,
        "maintenance": 3,
        "attack_skirmish": 4,
        "attack_melee": 6,
        "attack_pursue": 4,
        "defence_skirmish": 4.5,
        "defence_melee": 3,
        "defence_pursue": 2.5
    }
}

unit_list = []

for key in unit_stats.keys():
    unit_list.append(key)