def save_to_file(hero_name, hero_stats, hero_hp, hero_exp, inventory="", map_name="city", position=[3, 3]):
    file_name = f"saves/{hero_name}.txt"
    save_string = f"{hero_name},"
    for element in hero_stats:
        save_string += str(hero_stats[element]) + ","
    remaining_info = [hero_hp, hero_exp, inventory, map_name, position]
    for element in remaining_info:
        save_string += str(element) + ","
    with open(file_name, "w") as f:
        f.write(save_string)


def load_from_file(hero_name):
    file_name = f"saves/{hero_name}.txt"
    with open(file_name, "r") as f:
        contents = f.readline().strip()
    return contents


def check_for_existing_name(name, folder):
    file_name = f"{folder}/{name}.txt"
    try:
        f = open(file_name)
        f.close()
        return False
    except IOError:
        return True
