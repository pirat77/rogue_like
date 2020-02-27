import copy
import random
import display
import engine
import storage


def encounter(hero, npc):
    # TODO: Talking with npc
    try:
        if int(npc['condition']) < int(hero['exp']):
            display.npc_message(npc['special_message'], hero['name'], npc['name'])
            if npc['item']:
                add_item_to_inventory(hero, npc['item'])
            if npc['exp+']:
                hero['exp'] += int(npc['exp+'])
            npc['color'] = "white"
            engine.deacivate_field(npc)
        else:
            display.npc_message(npc['welcome_message'], hero['name'], npc['name'])
    except ValueError:
        if npc['condition'] in hero['inv']:
            display.npc_message(npc['special_message'], hero['name'], npc['name'])
            if npc['item']:
                add_item_to_inventory(hero, npc['item'])
            if npc['exp+']:
                hero['exp'] += int(npc['exp+'])
            engine.deacivate_field(npc)
        else:
            display.npc_message(npc['welcome_message'], hero['name'], npc['name'])


def enter_portal(hero, door):
    if int(hero["exp"]) < int(door['exp_needed']):
        display.print_message(f"You need {door['exp_needed']} to enter this portal.", True, False)
        return
    if door['key_needed'] == "":
        hero["position"] = [int(door['hero_position_y']), int(door['hero_position_x'])]
        hero['map'] = door['heading_to']
        # engine.game_play(hero, engine.load_map(door['heading_to'])[0], door['heading_to'])
        

def fight_mode(hero, enemy):
    # TODO: improve figt mode, special attacks from weapons, scalling of stats enemy,
    #        flash only hited, blood, shooting
    #       enemy choosing options, blood on face, scalling face of enemy
    hero = engine.convert_data_to_integers(hero)
    enemy = engine.convert_data_to_integers(enemy)
    hero_avatar = storage.load_avatar_from_file(hero["name"])
    enemy_avatar = storage.load_avatar_from_file(enemy["name"])
    hero_lvl = engine.calculate_hero_lvl(hero)
    for stat in enemy:
        if isinstance(enemy[stat], int) and stat != 'exp+':
            enemy[stat] = enemy[stat] * ((hero_lvl+5)//10)
    hero_avatar.append("")
    enemy_avatar.append("")
    fight_options = ["Quick attack", "Hard hit", "Defend"]
    fight_modes_dict = {"Quick attack": {"agility+": 25, "damage+": 0, "hp+": 0, "defence+": 0},
                        "Hard hit": {"agility+": 0, "damage+": 25, "hp+": 0, "defence+": 0},
                        "Defend": {"agility+": 10, "damage+": 0, "hp+": 0, "defence+": 25}}
    cursor_position = 0
    damage_taken = [0, 0]
    function_list_length = len(fight_options)
    while hero["hp"] > 0 and enemy["hp"] > 0:
        user_key = False
        while not user_key:
            your_hp, enemys_hp = display.display_fight_mode(hero, enemy)
            display.main_display([f"{hero['name']}, you are fighting with {enemy['name']}", your_hp, enemys_hp],
                                 left=hero_avatar, right=enemy_avatar, lower=display.display_menu("FIGHT", fight_options, cursor_position))
            cursor_position, user_key = engine.navigating_menus(function_list_length, cursor_position)
        damage_taken[0] = attack(hero, enemy, fight_modes_dict[fight_options[cursor_position]])
        damage_taken[1] = attack(enemy, hero, fight_modes_dict[random.choice(fight_options)])
        your_hp, enemys_hp = display.display_fight_mode(hero, enemy)

        damage_fight_mode(hero['name'], enemy['name'], damage_taken[0], damage_taken[1], hero_avatar, enemy_avatar)

        display.main_display([f"{hero['name']}, you are fighting with {enemy['name']}", your_hp, enemys_hp],
                             left=hero_avatar,
                             right=enemy_avatar,
                             lower=display.display_menu("FIGHT", fight_options, cursor_position))
    if hero['hp'] > 0:
        hero['exp'] += enemy['exp+']
        engine.deacivate_field(enemy)
    else:
        display.display_lose_game()


def damage_fight_mode(hero_name, enemy_name, damage_hero, damage_enemy, hero_avatar, enemy_avatar):
    avatar_length = 30
    if damage_hero:
        enemy_avatar[-1] = f"{enemy_name} lost {damage_hero} life"
    else:
        enemy_avatar[-1] = f"{enemy_name} dodged the hit"
    if damage_enemy:
        line = f"{hero_name} lost {damage_enemy} life"
        hero_avatar[-1] = line + ' ' * (avatar_length - len(line))
    else:
        line = f"{hero_name} dodged the hit"
        hero_avatar[-1] = line + ' ' * (avatar_length - len(line))


def attack(attacker, defender, mode):
    display.print_blank_screen()
    bonus_points = {"damage+": 0, "agility+": 0, "defence+": 0, "hp+": 0}
    # try:
    #     attacker["type"]
    # except KeyError:
    #     for key in bonus_points:
    #         bonus_points[key] += engine.check_inventory_for_extras(attacker, key)
    for key in bonus_points:
        bonus_points[key] += mode[key]
    hit_chance_ratio = attacker["DEX"] * 0.7 + attacker["INT"] * 0.3 + bonus_points["agility+"]
    dodge_chance_ratio = defender["DEX"] * 0.7 + defender["INT"] * 0.3 + bonus_points["agility+"]
    hit_attempt = float(hit_chance_ratio * random.randint(1, 9)/10)
    dodge_attempt = float(dodge_chance_ratio * random.randint(1, 9)/10)
    if hit_attempt > dodge_attempt:
        attack_ratio = attacker["STR"] * 0.7 + attacker["DEX"] * 0.3 + attacker["INT"] * 0.1
        + bonus_points["agility+"] + bonus_points["damage+"]
        defence_ratio = defender["CON"] * 0.7 + defender["STR"] * 0.3 + bonus_points["defence+"]
        hit_damage = float(attack_ratio * random.randint(1, 9)/10)
        defend_hit = float(defence_ratio * random.randint(1, 9)/10)
        damage_taken = hit_damage - defend_hit
        if damage_taken < 1:
            damage_taken = 1
        defender["hp"] = int(defender["hp"]) - damage_taken
        return int(damage_taken//1)


def add_item_to_inventory(hero, found_item):
    item_colected = copy.deepcopy(found_item)
    try:
        hero['inv'][item_colected['name']]['quantity'] += 1
    except KeyError:
        item_colected['quantity'] = 1
        hero['inv'][item_colected['name']] = item_colected
    engine.deacivate_field(found_item)
    if item_colected['name'] != 'gold':
        return engine.inventory(hero)
    else:
        return 0


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
        if element in location_values_dict:
            if location[location_values_dict[element]] == "Y":
                available_location_options.append(element)

    for element in available_location_options:
        func_list.append(possible_location_dict[element])
    available_location_options.insert(0, resume)
    func_list.insert(0, "RESUME")
    cursor_position = 0
    user_key = False
    function_list_lenght = len(available_location_options)
    while not user_key:
        display.main_display("", lower=display.display_menu(title, func_list, cursor_position))
        cursor_position, user_key = engine.navigating_menus(function_list_lenght, cursor_position)
    try:
        available_location_options[cursor_position](hero)
    except TypeError:
        available_location_options[cursor_position](hero, location)


def resume(hero):
    pass


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
        display.print_message("You don't have any priveleaged keys, get out of my way!", True, False)
        return 0
    user_key = False
    cursor_position = 0
    while not user_key:
        display.main_display("", lower=display.display_menu(title, available_wormholes, cursor_position))
        cursor_position, user_key = engine.navigating_menus(function_list_lenght, cursor_position)
    hero['map'] = unlock_dictionary[available_keys[cursor_position]][0]
    hero['position'][0] = unlock_dictionary[available_keys[cursor_position]][1][1]
    hero['position'][1] = unlock_dictionary[available_keys[cursor_position]][1][0]
    # engine.game_play(hero, engine.load_map(map_name)[0], map_name)
    # hero["position"] = [int(door['hero_position_y']), int(door['hero_position_x'])]


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
    print(hero['inv'])
    input()


def training_centre(hero):
    price = engine.calculate_hero_lvl(hero)
    if not ('gold' in hero['inv']):
        display.print_message(f"Not all that glitters is gold, I know. Stil... Come back when you have {price} gold.", True, False)
    elif hero['inv']['gold']['quantity'] < price:
        display.print_message(f"Not all that glitters is gold, I know. Stil... Come back when you have {price} gold.", True, False)
    else:
        spare_points = (hero['exp']//20)*hero['INT']//10
        hero['exp'] = hero['exp'] % 20
        bonus = engine.distribute_stat_points({"STR": hero['STR'], "CON": hero['CON'], "DEX": hero["DEX"],
                                               "INT": hero["INT"]}, spare_points)
        for key in bonus:
            hero[key] = bonus[key]
        hero['inv']['gold']['quantity'] -= price


def store(hero):
    print("wejscie do sklepu gdzie mozna cos kupic i doda do inventory")
    input()
