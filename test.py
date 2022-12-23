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

terrain = {
    "hill": {
        "archers": {
            "attack": 0.2,
            "defense": 0.5
        },
        "light_inf": {
            "attack": 0,
            "defense": 0.3
        },
        "pikemen": {
            "attack": 0.1,
            "defense": 0.2
        },
        "heavy_inf": {
            "attack": 0,
            "defense": 0.2
        },
        "light_cav": {
            "attack": 0,
            "defense": 0.15
        },
        "heavy_cav": {
            "attack": 0,
            "defense": 0
        },
        "horse_archers": {
            "attack": 0.1,
            "defense": 0.15
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
    "mountain": {
        "archers": {
            "attack": 0.5,
            "defense": 1
        },
        "light_inf": {
            "attack": 0,
            "defense": 1
        },
        "pikemen": {
            "attack": 0,
            "defense": 0.5
        },
        "heavy_inf": {
            "attack": 0,
            "defense": 0.5
        },
        "light_cav": {
            "attack": 0,
            "defense": 0
        },
        "heavy_cav": {
            "attack": 0,
            "defense": 0
        },
        "horse_archers": {
            "attack": 0,
            "defense": 0
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
    "stream": {
        "archers": {
            "attack": -0.1,
            "defense": -0.2
        },
        "light_inf": {
            "attack": -0.1,
            "defense": -0.2
        },
        "pikemen": {
            "attack": -0.15,
            "defense": -0.3
        },
        "heavy_inf": {
            "attack": -0.15,
            "defense": -0.3
        },
        "light_cav": {
            "attack": -0.2,
            "defense": -0.2
        },
        "heavy_cav": {
            "attack": -0.3,
            "defense": -0.3
        },
        "horse_archers": {
            "attack": -0.2,
            "defense": -0.2
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
       "forest": {
        "archers": {
            "attack": 0,
            "defense": 0.3
        },
        "light_inf": {
            "attack": 0.5,
            "defense": 0.3
        },
        "pikemen": {
            "attack": 0.1,
            "defense": 0.1
        },
        "heavy_inf": {
            "attack": 0,
            "defense": 0.1
        },
        "light_cav": {
            "attack": 0,
            "defense": 0.15
        },
        "heavy_cav": {
            "attack": 0,
            "defense": 0
        },
        "horse_archers": {
            "attack": 0.15,
            "defense": 0.15
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
    "desert": {
        "archers": {
            "attack": -0.05,
            "defense": -0.1
        },
        "light_inf": {
            "attack": -0.1,
            "defense": -0.1
        },
        "pikemen": {
            "attack": -0.15,
            "defense": -0.15
        },
        "heavy_inf": {
            "attack": -0.15,
            "defense": -0.15
        },
        "light_cav": {
            "attack": -0.125,
            "defense": -0.125
        },
        "heavy_cav": {
            "attack": -0.15,
            "defense": -0.15
        },
        "horse_archers": {
            "attack": -0.075,
            "defense": -0.125
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0.5,
            "defense": 0.5
        }
    },
    "stream": {
        "archers": {
            "attack": -0.1,
            "defense": -0.2
        },
        "light_inf": {
            "attack": -0.1,
            "defense": -0.2
        },
        "pikemen": {
            "attack": -0.15,
            "defense": -0.3
        },
        "heavy_inf": {
            "attack": -0.15,
            "defense": -0.3
        },
        "light_cav": {
            "attack": -0.2,
            "defense": -0.2
        },
        "heavy_cav": {
            "attack": -0.3,
            "defense": -0.3
        },
        "horse_archers": {
            "attack": -0.2,
            "defense": -0.2
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
        "river": {
        "archers": {
            "attack": -0.1,
            "defense": -0.15
        },
        "light_inf": {
            "attack": -0.15,
            "defense": -0.15
        },
        "pikemen": {
            "attack": -0.3,
            "defense": -0.3
        },
        "heavy_inf": {
            "attack": -0.3,
            "defense": -0.3
        },
        "light_cav": {
            "attack": -0.2,
            "defense": -0.2
        },
        "heavy_cav": {
            "attack": -0.3,
            "defense": -0.3
        },
        "horse_archers": {
            "attack": -0.2,
            "defense": -0.2
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
    "strait": {
        "archers": {
            "attack": -0.1,
            "defense": -0.15
        },
        "light_inf": {
            "attack": -0.15,
            "defense": -0.15
        },
        "pikemen": {
            "attack": -0.2,
            "defense": -0.2
        },
        "heavy_inf": {
            "attack": -0.2,
            "defense": -0.2
        },
        "light_cav": {
            "attack": -0.175,
            "defense": -0.175
        },
        "heavy_cav": {
            "attack": -0.2,
            "defense": -0.2
        },
        "horse_archers": {
            "attack": -0.125,
            "defense": -0.175
        },
        "war_ele": {
            "attack": 0,
            "defense": 0
        },
        "camel_cav": {
            "attack": 0,
            "defense": 0
        }
    },
    "amphibious": {
        "archers": {
            "attack": -0.1,
            "defense": -0.15
        },
        "light_inf": {
            "attack": -0.15,
            "defense": -0.15
        },
        "pikemen": {
            "attack": -0.2,
            "defense": -0.2
        },
        "heavy_inf": {
            "attack": -0.2,
            "defense": -0.2
        },
        "light_cav": {
            "attack": -0.2,
            "defense": -0.2
        },
        "heavy_cav": {
            "attack": -0.3,
            "defense": -0.3
        },
        "horse_archers": {
            "attack": -0.2,
            "defense": -0.2
        },
        "war_ele": {
            "attack": -0.15,
            "defense": -0.2
        },
        "camel_cav": {
            "attack": -0.2,
            "defense": -0.2
        }
    }
}


unit_list = []
terrain_list = []

for key in terrain.keys():
    terrain_list.append(key)

for key in unit_stats.keys():
    unit_list.append(key)

terrain_type = "hill"
unit_type = "archers"

#unit_type = unit_list.index(unit_type)
#terrain_type = terrain_list.index(terrain_type)
print(unit_type)
print(terrain[terrain_type][unit_type])
print(unit_stats[unit_type])
#terrain_modifiers = terrain[terrain_type][unit_type]
#print(terrain_modifiers)