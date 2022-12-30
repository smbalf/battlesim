import csv


terrain_stats = {}

# Open the CSV file and read the contents
with open('main/terrain_sheet.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    # Iterate over the rows in the CSV file
    for row in reader:
        # Get the terrain and unit names
        terrain = row["terrain"]
        unit = row["unit"]
        # If the terrain is not in the dictionary yet, add it
        if terrain not in terrain_stats:
            terrain_stats[terrain] = {}
        # If the unit is not in the terrain's dictionary yet, add it
        if unit not in terrain_stats[terrain]:
            terrain_stats[terrain][unit] = {}
        # Add the attribute-value pair to the unit's dictionary
        terrain_stats[terrain][unit][row["attribute"]] = float(row["value"])

terrain_list = [key for key in terrain_stats.keys()]

