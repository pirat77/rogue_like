import display
import controls
import sys


def navigating_menus(length_of_function_list, cursor_position):
    user_key = controls.getch()
    if user_key == "s" and cursor_position < (length_of_function_list - 1):
        cursor_position += 1
        return cursor_position, False
    elif user_key == "w" and cursor_position > 0:
        cursor_position -= 1
        return cursor_position, False
    elif user_key == "+":
        return cursor_position, True
    else:
        return cursor_position, False


def distribute_stat_points(character={"STR": 10, "CON": 10, "DEX": 10, "INT": 10}, spare_points=10):
    cursor_position = 0
    stats_names = ["STR", "CON", "DEX", "INT"]
    len_stat_names = len(stats_names)
    while spare_points > 0:
        display.display_distribute_stats(spare_points, character, cursor_position)
        cursor_position, user_key = navigating_menus(len_stat_names, cursor_position)
        if user_key:
            character[stats_names[cursor_position]] += 1
            spare_points -= 1
    return character


def moving_on_map(map_size, hero_position):
    DIRECTIONS = {'w': [-1, 0], 's': [1, 0], 'a': [0, -1], 'd': [0, 1]}
    player_position = hero_position
    button = controls.getch()
    if button not in ["w", "s", "a", "d", "+"]:
        return player_position, False
    if button == '+':
        return player_position, True
    for vector_component in range(len(player_position)):
        if not ((player_position[vector_component] + DIRECTIONS[button][vector_component] == -1)
                or (player_position[vector_component] + DIRECTIONS[button][vector_component] == map_size[vector_component])):
            player_position[vector_component] += DIRECTIONS[button][vector_component]
    return player_position, False


def load_map(map_name):
    PATH = sys.argv[0].strip("main.py") + "game_data/"
    try:
        with open(str(PATH + map_name + ".lvl"), "r") as f:
            map_string = f.read()
            map = eval(map_string)
            return map, map_name
    except FileNotFoundError:
        map = load_map(PATH + "my dungeon.lvl")
        return map, map_name


def convert_data_to_integers(dictionary):
    for key in dictionary:
        if isinstance(dictionary[key], str) and dictionary[key].isdigit():
            dictionary[key] = int(dictionary[key])
    return dictionary


def deacivate_field(object_reference):
    dead = {'symbol': '.', 'color': 'white', 'type': 'terrain', 'name': 'Empty space', 'can_enter?': 'Y'}
    keys = dead.keys()
    for key in keys:
        object_reference[key] = dead[key]


def moving_on_menu(map_size, hero_position):
    DIRECTIONS = {'w': [-1, 0], 's': [1, 0], 'a': [0, -1], 'd': [0, 1]}
    player_position = hero_position
    button = controls.getch()
    if button not in ["w", "s", "a", "d", "+"]:
        return player_position, False
    if button == '+':
        return player_position, True
    for vector_component in range(len(player_position)):
        if not ((player_position[vector_component] + DIRECTIONS[button][vector_component] == -1)
                or (player_position[vector_component] + DIRECTIONS[button][vector_component] == map_size[vector_component])):
            player_position[vector_component] += DIRECTIONS[button][vector_component]
    return player_position, False
