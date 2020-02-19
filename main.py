import controls
import os
import display
import common_functions
import storage
from termcolor import colored
import random
import ascii_art


def new_game():
    os.system("clear")
    # face configuration
    hero = {}
    hero["exp"] = 1
    
    hero["name"] = input("Enter a name: ")
    ascii_art.create_hero_avatar(hero["name"])
    valid_name = storage.check_for_existing_name(hero["name"], "saves")
    while not valid_name:
        hero["name"] = input("User name already exist, type another name: ")
        valid_name = storage.check_for_existing_name(hero["name"], "saves")
    # hero["stats"] = common_functions.distribute_stat_points()
    hero.update(common_functions.distribute_stat_points())

    hp_for_one_STR_point = 3
    hp_for_one_CON_point = 10
    hero_max_hp = hero['STR'] * hp_for_one_STR_point + hero['CON'] * hp_for_one_CON_point

    hero["hp"] = hero_max_hp
    hero["inv"] = {}
    hero["position"] = [3, 45]
    hero["map"] = "forest"
    hero["weapon_on"] = {'dmg+': 0, 'hp+': 0, 'defence+': 0, 'agility+': 0}
    hero["armor_on"] = {'dmg+': 0, 'hp+': 0, 'defence+': 0, 'agility+': 0}
    hero["amulet_on"] = {'dmg+': 0, 'hp+': 0, 'defence+': 0, 'agility+': 0}
    print(hero)
    storage.save_to_file(hero)
    # hero_full_info = [hero_name, hero_stats, hero_hp, hero_exp, "", "forest", [3, 45]]
    game_play(hero, common_functions.load_map("forest"))


def load_game():
    user_name = input("What character do you want to load? Type hero's name: ")
    if storage.check_for_existing_name(user_name, "saves"):
        display.print_hero_not_found()
    else:
        hero = eval(storage.load_from_file(user_name))
        game_play(hero, common_functions.load_map(hero["map"]))


def about():
    print("about")


def explore_menu():
    cursor_position = 0
    options_functions = [new_game, load_game, about, exit]
    display.display_menu("MAIN MENU", ["NEW GAME", "LOAD GAME", "ABOUT", "EXIT"])
    user_key = None
    while user_key != "+":
        user_key = controls.getch()
        if user_key == "s" and cursor_position < 3:
            cursor_position += 1
        elif user_key == "w" and cursor_position > 0:
            cursor_position -= 1
        elif user_key == "+":
            options_functions[cursor_position]()
            break
        display.display_menu("MAIN MENU", ["NEW GAME", "LOAD GAME", "ABOUT", "EXIT"], cursor_position)


def main():
    display.welcome()
    explore_menu()


def game_play(hero, map):
    map_size = [len(map), len(map[0])]
    hero_avatar = load_hero_avatar(hero["name"])
    in_menu = False
    while not in_menu:
        display.print_map(map, hero["position"], hero_avatar)
        previous_position_y, previous_position_x = int(hero["position"][0]), int(hero["position"][1])
        hero["position"], in_menu = common_functions.moving_on_map(map_size, hero["position"])
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


def enter_portal(hero, door):
    if int(hero["exp"]) < int(door['exp_needed']):
        display.print_more_exp_needed(door['exp_needed'])
        return 0
    if door['key_needed'] == "":
        hero["position"] = [int(door['hero_position_y']), int(door['hero_position_x'])]
        game_play(hero, common_functions.load_map(door['heading_to']))


def fight_mode(hero, enemy):
    hero = common_functions.convert_data_to_integers(hero)
    enemy = common_functions.convert_data_to_integers(enemy)
    fight_options = ["Quick attack", "Hard hit", "Defend"]
    while hero["hp"] > 0 and enemy["hp"] > 0:
        cursor_position = 0
        display.display_menu("FIGTH", fight_options, extras=display.display_fight_mode(hero, enemy))
        user_key = None
        while user_key != "+":
            user_key = controls.getch()
            if user_key == "s" and cursor_position < 2:
                cursor_position += 1
            elif user_key == "w" and cursor_position > 0:
                cursor_position -= 1
            elif user_key == "+":
                attack(hero, enemy, fight_options[cursor_position])
                break
            display.display_menu("FIGTH", ["Quick attack", "Hard hit", "Defend"],
                                 cursor_position, extras=display.display_fight_mode(hero, enemy))
        # random.choice[fight_options](enemy, hero)
        attack(enemy, hero, random.choice(fight_options))


# def quick_attack(attacker, defender, ):
#     hit_chance_ratio = attacker["DEX"] * 0.7 + attacker["INT"] * 0.3
#     dodge_chance_ratio = defender["DEX"] * 0.7 + defender["INT"] * 0.3
#     hit_attempt = float(hit_chance_ratio * random.randint(1, 9)/10)
#     dodge_attempt = float(dodge_chance_ratio * random.randint(1, 9)/10)
#     if hit_attempt < dodge_attempt:
#         print("missed")
#         return attacker, defender
#     else:
#         attack_ratio = attacker["STR"] * 0.7 + attacker["DEX"] * 0.3 + attacker["INT"] * 0.1
#         defence_ratio = defender["CON"] * 0.7 + defender["STR"] * 0.3

#         hit_damage = float(attack_ratio * random.randint(1, 9)/10)
#         defence_hit = float(defence_ratio * random.randint(1, 9)/10)
#         damage = hit_damage - defence_hit
#         if damage < 1:
#             damage = 1
#         defender["hp"] = int(defender["hp"]) - damage
#         return attacker, defender


def attack(attacker, defender, mode):
    attack_type_hit_chance = 1
    attack_type_damage = 1
    if mode == "Quick attack":
        attack_type_hit_chance = 7
    elif mode == "Hard hit":
        attack_type_damage = 5
    damage_bonus = 0
    agility_bonus = 0
    defence_bonus = 0

    try:
        attacker["type"]
    except KeyError:
        damage_bonus = check_inventory_for_extras(attacker, "dmg+")
        agility_bonus = check_inventory_for_extras(attacker, "agility+")
        defence_bonus = check_inventory_for_extras(attacker, "defence+")
        
    hit_chance_ratio = attacker["DEX"] * 0.7 + attacker["INT"] * 0.3 + agility_bonus
    dodge_chance_ratio = defender["DEX"] * 0.7 + defender["INT"] * 0.3 + agility_bonus
    hit_attempt = float(hit_chance_ratio * random.randint(1, 9)/10) * attack_type_hit_chance
    dodge_attempt = float(dodge_chance_ratio * random.randint(1, 9)/10)
    if hit_attempt < dodge_attempt:
        display.missed_attack(attacker)
    else:
        attack_ratio = attacker["STR"] * 0.7 + attacker["DEX"] * 0.3 + attacker["INT"] * 0.1 + agility_bonus + damage_bonus
        defence_ratio = defender["CON"] * 0.7 + defender["STR"] * 0.3 + defence_bonus
        hit_damage = float(attack_ratio * random.randint(1, 9)/10) * attack_type_damage
        defence_hit = float(defence_ratio * random.randint(1, 9)/10)
        damage = hit_damage - defence_hit
        if damage < 1:
            damage = 1
        defender["hp"] = int(defender["hp"]) - damage


def check_inventory_for_extras(hero, stat):
    now_using = ["weapon_on", "armor_on", "amulet_on"]
    items_bonus = 0
    for element in now_using:
        items_bonus += int(hero[element][stat])
    return items_bonus


def location_menu(hero, location):
    possible_locations_functions = []
    if location['save_point'] == 'Y':
        possible_locations_functions.append(save_point)
    if location['resting_point'] == 'Y':
        possible_locations_functions.append(resting_point)
    if location['storage_place'] == 'Y':
        possible_locations_functions.append(storage_place)
    if location['store'] == 'Y':
        possible_locations_functions.append(store)
    if location['training_centre'] == 'Y':
        possible_locations_functions.append(training_centre)
    cursor_position = 0
    display.display_location_menu(location, possible_locations_functions)
    user_key = None
    while user_key != "+":
        user_key = controls.getch()
        if user_key == "s" and cursor_position < len(possible_locations_functions):
            cursor_position += 1
        elif user_key == "w" and cursor_position > 0:
            cursor_position -= 1
        elif user_key == "+":
            possible_locations_functions[cursor_position]()
            break
        display.display_location_menu(location, possible_locations_functions, cursor_position)


def save_point(hero, location):
    print("funkcja zapisujaca aktualna rozgrywke")


def resting_point(hero, location):
    hp_for_one_STR_point = 3
    hp_for_one_CON_point = 10
    hero_max_hp = hero['STR'] * hp_for_one_STR_point + hero['CON'] * hp_for_one_CON_point
    healing_point = 0.15 * hero_max_hp
    if hero['hp'] < healing_point:
        hero['hp'] = hero_max_hp
    return hero


def storage_place(hero, location):
    print("pokaż mi swoje towary")
    print("inventory gracza i storage do ktorego mozna odlozyc rzeczy")


def training_centre(hero, location):
    print("trenowanie jakiejś statystyki np STR za golda")


def store(hero, location):
    print("wejscie do sklepu gdzie mozna cos kupic i doda do inventory")


main()
