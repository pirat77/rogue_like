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


def inventory(hero):
    wearables = {'weapon': 'weapon_on', 'armor': 'armor_on', 'amulet': 'amulet_on'}
    # TODO: dealing with single use items
    user_key = 0
    cursor_position = 0
    capacity = (int(hero["STR"]) + int(hero["CON"])) / 2
    items_worn, key_names, item_display, weight = extract_info_from_inventory(hero)
    function_list_lenght = len(item_display)
    title, extras, extras_2 = set_title__and_extras(weight, capacity)
    if not key_names:
        display.print_message('Your inventory is empty yet', wait=True, press_any_key=False)
        return
    while not user_key:
        display_menu = display.display_menu(title, item_display, cursor_position, extras, extras_2)
        display.main_display(items_worn, lower=display_menu)
        cursor_position, user_key = navigating_menus(function_list_lenght, cursor_position)
    if weight > capacity:
        if hero["inv"][key_names[cursor_position]]['quantity'] > 1:
            hero["inv"][key_names[cursor_position]]['quantity'] -= 1
        else:
            hero["inv"].pop(key_names[cursor_position])
        inventory(hero)
    if hero['inv'][key_names[cursor_position]]['used_for'] in wearables:
        if hero['inv'][key_names[cursor_position]]['used_for'] == 'amulet' and int(hero['inv'][key_names[cursor_position]]['INT needed']) <= hero['INT']:            
            hero[wearables[hero['inv'][key_names[cursor_position]]['used_for']]] = hero['inv'][key_names[cursor_position]]['name']
            display.print_message(f"You become empowered by force of fine {hero['inv'][key_names[cursor_position]]['used_for']}, {key_names[cursor_position]}", False, True)
        elif int(hero['inv'][key_names[cursor_position]]['STR needed']) <= hero['STR']:
            hero[wearables[hero['inv'][key_names[cursor_position]]['used_for']]] = hero['inv'][key_names[cursor_position]]['name']
            display.print_message(f"You become empowered by force of fine {hero['inv'][key_names[cursor_position]]['used_for']}, {key_names[cursor_position]}", False, True)
        else:
            display.print_message("You can't wear this item, you need higher stats to do this.", False, True)
        return


def extract_info_from_inventory(hero):
    weight = 0.0
    item_display = []
    key_names = []
    items_worn = [f'Items {hero["name"]} is wearing now:']
    for element in hero['inv']:
        if hero['weapon_on'] == element or hero['armor_on'] == element or hero['amulet_on'] == element:
            items_worn.append(str(element))
            weight += float(hero['inv'][element]['weight'])*hero['inv'][element]['quantity']
            if hero['inv'][element]['quantity'] > 1:
                item_display.append(str(hero['inv'][element]['quantity'] - 1)+" * "+str(element))
                key_names.append(str(element))
        else:
            weight += float(hero['inv'][element]['weight'])*hero['inv'][element]['quantity']
            item_display.append(str(hero['inv'][element]['quantity'])+" * "+str(element))
            key_names.append(str(element))
    if len(items_worn) == 1:
        items_worn[0] = "You are not wearing any items."
    return items_worn, key_names, item_display, weight


def set_title__and_extras(weight, capacity):
    weight = weight // 1
    if weight < capacity:
        title = "This is your belongings:"
    else:
        title = "You have to throw away something"
    extras = ' '
    extras_2 = f'Your capacity: {weight} / {capacity}'
    return title, extras, extras_2


def calculate_hero_lvl(hero):
    list_of_stats = ['STR', "CON", 'DEX', 'INT']
    total_stats = 0
    for element in list_of_stats:
        total_stats += hero[element]
    lvl = (total_stats - 40) // 10
    return lvl


def check_inventory_for_extras(hero, stat):
    now_using = ["weapon_on", "armor_on", "amulet_on"]
    items_bonus = 0
    for element in now_using:
        items_bonus += int(hero[element][stat])
    return items_bonus
