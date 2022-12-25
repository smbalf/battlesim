import csv


unit_stats = {}

with open('test/test_unit_sheet.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        unit = row['unit']
        unit_data = {
            "unit_cost": int(row['unit_cost']),
            "soldiers": int(row['soldiers']),
            "morale": float(row['morale']),
            "attack_skirmish": float(row['attack_skirmish']),
            "attack_melee": float(row['attack_melee']),
            "attack_pursue": float(row['attack_pursue']),
            "defence_skirmish": float(row['defence_skirmish']),
            "defence_melee": float(row['defence_melee']),
            "defence_pursue": float(row['defence_pursue'])
            }
        # Write units and stats to unit_stats dict
        unit_stats[unit] = unit_data

unit_list = [key for key in unit_stats.keys()]
