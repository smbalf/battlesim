from terrain_file import terrain, terrain_list


def choose_terrain():
    print("Choose the terrain for the battle:")
    for i, t in enumerate(terrain.keys()):
        print(f"{i}: {t}")
    terrain_choice = input("Choose the terrain for the battle: ")
    try:
        terrain_choice = int(terrain_choice)
        if 0 <= terrain_choice <= len(terrain_list):
            chosen_terrain = terrain_list[terrain_choice]
            print(f'The battle terrain will be: {chosen_terrain}')
            return chosen_terrain
        elif terrain_choice > len(terrain_list):
            choose_terrain()
    except ValueError:
        choose_terrain()


#choose_terrain()