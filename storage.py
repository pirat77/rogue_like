def save_to_file(hero):
    file_name = f"saves/{hero['name']}.txt"
    save_string = ""
    save_string += str(hero)
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
