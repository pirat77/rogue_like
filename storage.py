import sys


def save_to_file(hero):
    PATH = sys.argv[0].strip("main.py")
    file_name = f"{PATH}saves/{hero['name']}.txt"
    save_string = ""
    save_string += str(hero)
    with open(file_name, "w") as f:
        f.write(save_string)


def load_from_file(hero_name):
    PATH = sys.argv[0].strip("main.py")
    print(PATH)
    file_name = f"{PATH}saves/{hero_name}.txt"
    with open(file_name, "r") as f:
        contents = f.readline().strip()
    return contents


def check_for_existing_name(name, folder):
    PATH = sys.argv[0].strip("main.py")
    file_name = f"{PATH}{folder}/{name}.txt"
    try:
        f = open(file_name)
        f.close()
        return False
    except IOError:
        return True


def save_avatar_to_file(hero_name, hero_face):
    PATH = sys.argv[0].strip("main.py")
    file_name = f"{PATH}saves/{hero_name}_avatar.txt"
    string_hero_face = "\n".join(hero_face)
    with open(file_name, "w") as f:
        f.write(string_hero_face)


def load_avatar_from_file(hero_name):
    PATH = sys.argv[0].strip("main.py")
    file_name = f"{PATH}saves/{hero_name}_avatar.txt"
    with open(file_name, "r") as f:
        loaded_avatar = f.read()
        hero_avatar_loaded = loaded_avatar.split("\n")
        # hero_avatar_loaded = [list(element) for element in hero_avatar_loaded]
    return hero_avatar_loaded
