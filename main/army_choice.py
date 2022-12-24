import os
from unit_file import unit_stats


army_one = {}
army_two = {}
default_composition = {'archers': 15, 'light_inf': 10, 'heavy_inf': 10, 'light_cav': 5, 'heavy_cav': 3}
#GOLD COST IS 100

def choose_units(army_one, army_two):
    gold_one = 100
    gold_two = 100

    # Choose units for army one
    print(f"Army one, you have {gold_one} gold remaining. choose your units:")
    i = 0
    for unit, stats in unit_stats.items():
        print(f"{i}: {unit} (maintenance cost: {stats['maintenance']})")
        i += 1

    while gold_one > 0:
        try:
            choice = input("Enter the number of the unit you want to add to your army (or 'done' when finished/for default):\n")
            choice = choice.lower()
            if choice == "done":
                break
            elif int(choice) in range(len(unit_stats)):
                unit = list(unit_stats.keys())[int(choice)]
                number = int(input(f"How many {unit} would you like?\n"))
                cost = unit_stats[unit]["maintenance"] * number
                if gold_one - cost >= 0:
                    if unit in army_one:
                        gold_one -= cost
                        army_one[unit] += number
                        print(f"Added {number} {unit} to army one for {cost} gold. {gold_one} gold remaining.")
                    else:
                        gold_one -= cost
                        army_one[unit] = number
                        print(f"Added {number} {unit} to army one for {cost} gold. {gold_one} gold remaining.")
                else:
                    print("Not enough gold. Please choose a different unit or type 'done' to finish.")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please try again.")

    # Choose units for army two
    print(f"\nArmy two, you have {gold_two} gold remaining. choose your units:")
    i = 0
    for unit, stats in unit_stats.items():
        print(f"{i}: {unit} (maintenance cost: {stats['maintenance']})")
        i += 1

    while gold_two > 0:
        try:
            choice = input("Enter the number of the unit you want to add to your army (or 'done' when finished/for default):\n")
            choice = choice.lower()
            if choice == "done":
                break
            elif int(choice) in range(len(unit_stats)):
                unit = list(unit_stats.keys())[int(choice)]
                number = int(input(f"How many {unit} would you like?\n"))
                cost = unit_stats[unit]["maintenance"] * number
                if gold_two - cost >= 0:
                    if unit in army_two:
                        gold_two -= cost
                        army_two[unit] += number
                        print(f"Added {number} {unit} to army two for {cost} gold. {gold_two} gold remaining.")
                    else:
                        gold_two -= cost
                        army_two[unit] = number
                        print(f"Added {number} {unit} to army two for {cost} gold. {gold_two} gold remaining.")
                else:
                    print("Not enough gold. Please choose a different unit or type 'done' to finish.")
        except ValueError:
            print("Invalid choice. Please try again.")
    
    os.system('cls')
    if bool(army_one) == False:
        print("Army one using default composition...")
        army_one = default_composition
        gold_one -= 100
    if bool(army_two) == False:
        print("Army two using default composition...")
        army_two = default_composition
        gold_two -= 100

    return army_one, army_two


#choose_units(army_one, army_two)