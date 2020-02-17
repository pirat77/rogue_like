def save_to_file(hero_name, hero_stats, hero_hp, hero_exp, inventory=""):
    file_name = f"saves/{hero_name}.txt"
    save_string = f"{hero_name},"
    for element in hero_stats:
        save_string += str(hero_stats[element]) + ","
    save_string += str(hero_hp) + ","
    save_string += str(hero_exp) + "|"
    save_string += str(inventory)
    with open(file_name, "w") as f:
        f.write(save_string)


def load_from_file(hero_name):
    file_name = f"saves/{hero_name}.txt"
    with open(file_name, "r") as f:
        contents = f.readline().strip()
    return contents


def check_for_existing_name(hero_name):
    file_name = f"saves/{hero_name}.txt"
    try:
        f = open(file_name)
        f.close()
        return False
    except IOError:
        return True
