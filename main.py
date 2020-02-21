import controls
import display
import common_functions
import storage
import random
import ascii_art
import copy


def new_game():
    columns = display.config()
    hero = {}
    hero["exp"] = 1
    display.print_new_game_ask_for_input(columns)
    hero["name"] = input((int(columns/2)) * " ")
    valid_name = storage.check_for_existing_name(hero["name"], "saves")
    while not valid_name:
        hero["name"] = input("User name already exist, type another name: ")
        valid_name = storage.check_for_existing_name(hero["name"], "saves")
    storage.save_avatar_to_file(hero["name"], display.create_hero_avatar(hero["name"]))
    hero.update(common_functions.distribute_stat_points())
    hp_for_one_STR_point = 3
    hp_for_one_CON_point = 10
    hero_max_hp = hero['STR'] * hp_for_one_STR_point + hero['CON'] * hp_for_one_CON_point
    hero["hp"] = hero_max_hp
    hero["inv"] = {}
    hero["position"] = [10, 10]
    hero["map"] = "city"
    hero["weapon_on"] = {'dmg+': 0, 'hp+': 0, 'defence+': 0, 'agility+': 0}
    hero["armor_on"] = {'dmg+': 0, 'hp+': 0, 'defence+': 0, 'agility+': 0}
    hero["amulet_on"] = {'dmg+': 0, 'hp+': 0, 'defence+': 0, 'agility+': 0}
    print(hero)
    storage.save_to_file(hero)
    game_play(hero, common_functions.load_map("city")[0], "city")


def load_game():
    columns = display.config()
    display.print_load_ask_for_input(columns)
    user_name = input((int(columns/2)) * " ")
    if storage.check_for_existing_name(user_name, "saves"):
        display.print_hero_not_found()
    else:
        hero = eval(storage.load_from_file(user_name))
        game_play(hero, common_functions.load_map(hero["map"])[0], hero['map'])


def about(in_game_already):
    upper = ['', '', 'Good Luck']
    lower = [' ', ' ', 'Welcome to Hell\'O\' Word',
            'This game has been created', 'in three days,',
            'by top_level team of hackers', 
            'from NSA', 'Your objective is simple:', 
            'You have to save the word', 
            'Kill monsters, love widows,', 
            'gather gold,', 
            'explore dungeons', 
            'Game controls are as easy', 
            'as it can be:', 'w - go north', 
            's - go south', 
            'a - go east', 
            'd - go west', 
            '+ - accept options in menu', 
            'follow instructions on the screen']
    display.main_display(upper, lower)
    input()
    explore_menu(in_game_already)


def explore_menu(in_game_already=True, hero={}):
    cursor_position = 0
    title = "MAIN MENU"
    options_functions = [new_game, load_game, about, exit]
    options_display = {new_game: "NEW GAME", load_game: "LOAD GAME", about: "ABOUT", exit: "EXIT"}
    if in_game_already:
        options_functions.insert(0, resume)
        options_functions.insert(0, inventory)
        options_display.update({resume: "RESUME", inventory: "INVENTORY"})
    function_list_lenght = len(options_functions)
    user_key = False
    options_names = [options_display[x] for x in options_functions]
    while not user_key:
        display_menu = display.display_menu(title, options_names, cursor_position)
        display.main_display([""], lower=display_menu)
        cursor_position, user_key = common_functions.navigating_menus(function_list_lenght, cursor_position)
    try:
        options_functions[cursor_position]()
    except TypeError:
        if cursor_position == 0:
            options_functions[cursor_position](hero)
        else:
            options_functions[cursor_position](in_game_already)


def inventory(hero):
    wearables = {'weapon': 'weapon_on', 'armor': 'armor_on', 'amulet': 'amulet_on'}
    wearables_bonuses = ['dmg+', 'hp+', 'defence+', 'agility+']
    user_key = 0
    cursor_position = 0
    weight = 0.0
    item_display = []
    key_names = []
    capacity = (int(hero["STR"]) + int(hero["CON"])) / 2 
    for element in hero['inv']:
        weight += float(hero['inv'][element]['weight'])*hero['inv'][element]['quantity']
        item_display.append(str(hero['inv'][element]['quantity'])+" * "+str(element))
        key_names.append(str(element))
    function_list_lenght = len(item_display)
    weight = weight // 1
    if weight < capacity:
        title = "This is your belongings:"
    else:
        title = "You have to throw away something"
    extras = ' '
    extras_2 = f'Your capacity: {weight} / {capacity}'
    if not key_names:
        display.display_empty_inventory()
        return
    while not user_key:
        display_menu = display.display_menu(title, item_display, cursor_position, extras, extras_2)
        display.main_display([""], lower=display_menu)
        cursor_position, user_key = common_functions.navigating_menus(function_list_lenght, cursor_position)
    if weight > capacity:
        if hero["inv"][key_names[cursor_position]]['quantity'] > 1:
            hero["inv"][key_names[cursor_position]]['quantity'] -= 1
        else:
            hero["inv"].pop(key_names[cursor_position])
        inventory(hero)
    if hero['inv'][key_names[cursor_position]]['used_for'] in wearables:
        for bonus in wearables_bonuses:
            hero[f"{hero['inv'][key_names[cursor_position]]['used_for']}_on"][bonus] = int(hero['inv'][key_names[cursor_position]][bonus])
            print(f"You become empowered by force of fine {hero['inv'][key_names[cursor_position]]['used_for']}, {key_names[cursor_position]}")
            input()
            return 


def add_item_to_inventory(hero, found_item):
    item_colected = copy.deepcopy(found_item)
    try:
        hero['inv'][item_colected['name']]['quantity'] += 1
    except KeyError:
        item_colected['quantity'] = 1
        hero['inv'][item_colected['name']] = item_colected
    common_functions.deacivate_field(found_item)
    return inventory(hero)
    

def main():
    ascii_art.welcome()
    explore_menu(False)


def game_play(hero, map, map_name):
    map_size = [len(map), len(map[0])]
    hero_avatar = storage.load_avatar_from_file(hero["name"])
    upper_title = ["\n", f"{hero['name']}, you are now exploring {map_name}.", ""]
    in_menu = False
    while not in_menu:
        display.main_display(upper_title, left=hero_avatar, right=display.print_map(map, hero['position']), lower=display.display_stats(hero),
                             right_length=map_size[1])
        previous_position_y, previous_position_x = int(hero["position"][0]), int(hero["position"][1])
        hero["position"], in_menu = common_functions.moving_on_map(map_size, hero["position"])
        if in_menu:
            in_menu = explore_menu(True, hero=hero)
        field_type = map[hero["position"][0]][hero["position"][1]]['type']
        if field_type == 'terrain':
            if map[hero["position"][0]][hero["position"][1]]['can_enter?'] == 'N':
                hero["position"] = [previous_position_y, previous_position_x]
        elif field_type == 'enemy':
            fight_mode(hero, map[hero["position"][0]][hero["position"][1]])
        elif field_type == 'door':
            enter_portal(hero, map[hero["position"][0]][hero["position"][1]])
        elif field_type == 'location':
            location_menu(hero, map[hero["position"][0]][hero["position"][1]])
        elif field_type == 'npc':
            encounter(hero, map[hero["position"][0]][hero["position"][1]])
        elif field_type == 'item':
            add_item_to_inventory(hero, map[hero['position'][0]][hero['position'][1]])


def resume(in_game_already):
    return in_game_already


def encounter(hero, npc):
    try:
        if int(npc['condition']) < int(hero['exp']):
            display.npc_message(npc['special_message'], hero['name'], npc['name'])
            if npc['item']:
                add_item_to_inventory(hero, npc['item'])
            if npc['exp+']:
                hero['exp'] += int(npc['exp+'])
            npc['color'] = "white"
            common_functions.deacivate_field(npc)

        else:
            display.npc_message(npc['welcome_message'], hero['name'], npc['name'])     
    except ValueError:
        if npc['condition'] in hero['inv']:
            display.npc_message(npc['special_message'], hero['name'], npc['name'])
            if npc['item']:
                add_item_to_inventory(hero, npc['item'])
            if npc['exp+']:
                hero['exp'] += int(npc['exp+'])
            common_functions.deacivate_field(npc)
        else:
            display.npc_message(npc['welcome_message'], hero['name'], npc['name'])


def enter_portal(hero, door):
    if int(hero["exp"]) < int(door['exp_needed']):
        display.print_more_exp_needed(door['exp_needed'])
        return 0
    if door['key_needed'] == "":
        hero["position"] = [int(door['hero_position_y']), int(door['hero_position_x'])]
        game_play(hero, common_functions.load_map(door['heading_to'])[0], door['heading_to'])


def fight_mode(hero, enemy):
    hero = common_functions.convert_data_to_integers(hero)
    enemy = common_functions.convert_data_to_integers(enemy)
    hero_avatar = storage.load_avatar_from_file(hero["name"])
    enemy_avatar = storage.load_avatar_from_file(enemy["name"])
    fight_options = ["Quick attack", "Hard hit", "Defend"]
    fight_modes_dict = {"Quick attack": {"agility+": 25, "dmg+": 0, "hp+": 0, "defence+": 0},
                        "Hard hit": {"agility+": 0, "dmg+": 25, "hp+": 0, "defence+": 0},
                        "Defend": {"agility+": 0, "dmg+": 0, "hp+": 0, "defence+": 0}}
    cursor_position = 0
    while hero["hp"] > 0 and enemy["hp"] > 0:
        damage_taken = 0
        user_key = None
        while user_key != "+":
            your_hp, enemys_hp = display.display_fight_mode(hero, enemy)
            display.main_display([f"{hero['name']}, you are fighting with {enemy['name']}", your_hp, enemys_hp],
                                 left=hero_avatar, right=enemy_avatar, lower=display.display_menu("FIGHT", fight_options, cursor_position))
            user_key = controls.getch()
            if user_key == "s" and cursor_position < 2:
                cursor_position += 1
            elif user_key == "w" and cursor_position > 0:
                cursor_position -= 1
            elif user_key == "+":
                damage_taken = attack(hero, enemy, fight_modes_dict[fight_options[cursor_position]])
                break                
        damage_taken = attack(enemy, hero, fight_modes_dict[random.choice(fight_options)])
        your_hp, enemys_hp = display.display_fight_mode(hero, enemy)
        display.main_display([f"{hero['name']}, you are fighting with {enemy['name']}", your_hp, enemys_hp],
                             left=hero_avatar, right=enemy_avatar, lower=display.display_menu("FIGHT", fight_options, cursor_position))
    if hero['hp'] > 0:
        hero['exp'] += enemy['exp+']
        common_functions.deacivate_field(enemy)
    else:
        display.display_lose_game()


def attack(attacker, defender, mode):
    display.print_blank_screen()
    bonus_points = {"dmg+": 0, "agility+": 0, "defence+": 0, "hp+": 0}
    try:
        attacker["type"]
    except KeyError:
        for key in bonus_points:
            bonus_points[key] += check_inventory_for_extras(attacker, key)
    for key in bonus_points:
        bonus_points[key] += mode[key]
    hit_chance_ratio = attacker["DEX"] * 0.7 + attacker["INT"] * 0.3 + bonus_points["agility+"]
    dodge_chance_ratio = defender["DEX"] * 0.7 + defender["INT"] * 0.3 + bonus_points["agility+"]
    hit_attempt = float(hit_chance_ratio * random.randint(1, 9)/10)
    dodge_attempt = float(dodge_chance_ratio * random.randint(1, 9)/10)
    if hit_attempt < dodge_attempt:
        display.missed_attack(attacker["name"])
    else:
        attack_ratio = attacker["STR"] * 0.7 + attacker["DEX"] * 0.3 + attacker["INT"] * 0.1 + bonus_points["agility+"] + bonus_points["dmg+"]
        defence_ratio = defender["CON"] * 0.7 + defender["STR"] * 0.3 + bonus_points["defence+"]
        hit_damage = float(attack_ratio * random.randint(1, 9)/10)
        defend_hit = float(defence_ratio * random.randint(1, 9)/10)
        damage_taken = hit_damage - defend_hit
        if damage_taken < 1:
            damage_taken = 1
        defender["hp"] = int(defender["hp"]) - damage_taken
        return damage_taken


def check_inventory_for_extras(hero, stat):
    now_using = ["weapon_on", "armor_on", "amulet_on"]
    items_bonus = 0
    for element in now_using:
        items_bonus += int(hero[element][stat])
    return items_bonus


def location_menu(hero, location):
    func_list = []
    available_location_options = []
    title = f"Welcome to {location['name']}! Take your time"
    possible_locations_functions = [save_point, resting_point, storage_place, store, training_centre, wormhole]
    location_values_dict = {save_point: "save_point", resting_point: "resting_point", storage_place: "storage_place", 
                            store: 'store', training_centre: 'training_centre', wormhole: 'wormhole'}
    possible_location_dict = {save_point: 'SAVE GAME', resting_point: 'HEAL ME!',
                              storage_place: 'OPEN STORAGE', store: 'SHOW ME YOUR GOODS',
                              training_centre: 'TRAIN ABILITIES', wormhole: "WORMHOLE"}
    for element in possible_locations_functions:
        try:
            if location[location_values_dict[element]] == "Y":
                available_location_options.append(element)
        except KeyError:
            pass
    for element in available_location_options:
        func_list.append(possible_location_dict[element])
    cursor_position = 0
    user_key = False
    function_list_lenght = len(available_location_options)
    while not user_key:
        display.main_display("", lower=display.display_menu(title, func_list, cursor_position))
        cursor_position, user_key = common_functions.navigating_menus(function_list_lenght, cursor_position)
    try:
        available_location_options[cursor_position](hero)
    except TypeError:
        available_location_options[cursor_position](hero, location)


def wormhole(hero):
    name = hero['name']
    title = f'Petty {name} are you ready to enter the wormhole?'
    key_list = ["brass lamp", "magic key", "crystal", "arkenstone", "microchip", "oak leaf"]
    unlock_dictionary = {"arkenstone": ["dungeon", [18, 3]], "crystal": ["mine", [14, 8]],
                         "brass lamp": ["desert", [2, 0]], "oak leaf": ["mountains", [1, 10]],
                         "microchip": ["cyberworld", [4, 6]], "magic key": ["dreamland", [6, 8]]}
    available_wormholes = []
    available_keys = []
    for element in hero['inv']:
        if element in key_list:
            available_wormholes.append(unlock_dictionary[element][0])
            available_keys.append(element)
    cursor_position = 0
    user_key = False
    function_list_lenght = len(available_wormholes)
    if not available_wormholes:
        display.display_no_wormhole_keys()
        return 0
    user_key = False
    cursor_position = 0
    while not user_key:
        display.main_display("", lower=display.display_menu(title, available_wormholes, cursor_position))
        cursor_position, user_key = common_functions.navigating_menus(function_list_lenght, cursor_position)
    map_name = unlock_dictionary[available_keys[cursor_position]][0]
    hero['position'][0] = unlock_dictionary[key_list[cursor_position]][1][0]
    hero['position'][1] = unlock_dictionary[key_list[cursor_position]][1][1]
    game_play(hero, common_functions.load_map(map_name)[0], map_name)


def save_point(hero, location):
    columns = display.config()
    storage.save_to_file(hero)
    if location['name'] == 'home':
        cheat = input("Game saved".center(columns)).lower()
        if cheat == 'dupa':
            hero['STR'] = 999
            hero['CON'] = 999
            hero['DEX'] = 999
            hero['INT'] = 999
    else:
        print("Game saved".center(columns))
        input()
    

def resting_point(hero):
    columns = display.config()
    hp_for_one_STR_point = 3
    hp_for_one_CON_point = 10
    hero_max_hp = hero['STR'] * hp_for_one_STR_point + hero['CON'] * hp_for_one_CON_point
    healing_point = 0.15 * hero_max_hp
    if hero['hp'] < healing_point:
        hero['hp'] = hero_max_hp
    else:
        print("You look healthy.".center(columns))
        input()
    return hero


def storage_place(hero, location):
    print("pokaż mi swoje towary")
    print("inventory gracza i storage do ktorego mozna odlozyc rzeczy")
    input()


def training_centre(hero):
    price = display.calculate_hero_lvl(hero)
    if not ('gold' in hero['inv']):
        display.not_enough_gold(price)
    elif hero['inv']['gold']['quantity'] < price:
        display.not_enough_gold(price)
    else:
        spare_points = (hero['exp']//20)*hero['INT']//10
        hero['exp'] = hero['exp'] % 20
        bonus = common_functions.distribute_stat_points({"STR": hero['STR'], "CON": hero['CON'], "DEX": hero["DEX"],
                                                         "INT": hero["INT"]}, spare_points)
        for key in bonus:
            hero[key] = bonus[key]
        hero['inv']['gold']['quantity'] -= price


def store(hero):
    print("wejscie do sklepu gdzie mozna cos kupic i doda do inventory")
    input()


main()
