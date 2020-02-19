import controls
import os
import display
import common_functions
import storage
from termcolor import colored
import random


SAVE_NAME = 0
SAVE_STATS = 1
SAVE_HP = 2
SAVE_EXP = 3
SAVE_INVENTORY = 4
SAVE_MAP_NAME = 5
SAVE_POSITION = 6


def new_game():
    os.system("clear")
    # face configuration
    hero = {}
    hero["exp"] = 1
    
    hero["name"] = input("Enter a name: ")
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
    in_menu = False
    while not in_menu:
        display.print_map(map, hero["position"])
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
        elif field_type == 'npc'
            encounter(hero, map[hero["position"][0]][hero["position"][1]])
        elif field_type == 'item'
            inventory(hero, map[hero['position'][0]][hero['position'][1]]['name'])


def encounter(hero, npc)
    try:
        if int(npc['condition']) < int(hero['exp'])
            display.npc_message(npc['special_message'])
            if npc['item']:
                inventory(hero, map[hero['position'][0]][hero['position'][1]]['name'])
            if npc['exp+']:
                hero['exp'] += int(npc['exp+'])
        else:
            display.npc_message(npc['welcome_message'])     

    except:        
        if npc['condition'] in hero['inv']
            display.npc_message(npc['special_message'])
            if npc['item']:
                inventory(hero, map[hero['position'][0]][hero['position'][1]]['name'])
            if npc['exp+']:
                hero['exp'] += int(npc['exp+'])
        else:
            display.npc_message(npc['welcome_message'])

    "npc": ["welcome_message", "condition", "special_message", "item", "exp+"]

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
    fight_options = [quick_attack, hard_hit, defend]
    while hero["hp"] > 0 and enemy["hp"] > 0:
        cursor_position = 0
        display.display_menu("FIGTH", ["Quick attack", "Hard hit", "Defence"], extras=display.display_fight_mode(hero, enemy))
        user_key = None
        while user_key != "+":
            user_key = controls.getch()
            if user_key == "s" and cursor_position < 2:
                cursor_position += 1
            elif user_key == "w" and cursor_position > 0:
                cursor_position -= 1
            elif user_key == "+":
                fight_options[cursor_position](hero, enemy)
                break
            display.display_menu("FIGTH", ["Quick attack", "Hard hit", "Defence"],
                                 cursor_position, extras=display.display_fight_mode(hero, enemy))
        # random.choice[fight_options](enemy, hero)
        quick_attack(enemy, hero)


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
    extra_hit_chance = 1
    extra_damage = 1

    if mode == "quick_attack":
        extra_hit_chance = 7
    elif mode == "hard_hit":
        extra_damage = 3
    hit_chance_ratio = attacker["DEX"] * 0.7 + attacker["INT"] * 0.3
    dodge_chance_ratio = defender["DEX"] * 0.7 + defender["INT"] * 0.3
    hit_attempt = float(hit_chance_ratio * random.randint(1, 9)/10) * extra_hit_chance
    dodge_attempt = float(dodge_chance_ratio * random.randint(1, 9)/10)
    if hit_attempt < dodge_attempt:
        print("missed")
    else:
        attack_ratio = attacker["STR"] * 0.7 + attacker["DEX"] * 0.3 + attacker["INT"] * 0.1
        defence_ratio = defender["CON"] * 0.7 + defender["STR"] * 0.3
        hit_damage = float(attack_ratio * random.randint(1, 9)/10) * extra_damage
        defence_hit = float(defence_ratio * random.randint(1, 9)/10)
        damage = hit_damage - defence_hit
        if damage < 1:
            damage = 1
        defender["hp"] = int(defender["hp"]) - damage


# def check_for_


def hard_hit(attacker, defender):
    pass


def defend(attacker, defender):
    pass


def location_menu(hero, location):
    possible_locations_functions = []
    if location['save_point'] == 'Y':
        possible_locations_functions.append(save_point)
    if location['resting_point'] == 'Y':
        possible_locations_functions.append(resting_point)
    if location['storage_place'] == 'Y':
        possible_locations_functions.append(storage_place)
    if location['store'] == 'Y':
        possible_locations_functions.append(storage_place)
    if location['training_centre'] == 'Y':
        possible_locations_functions.append(storage_place)
    # possible_locations_functions = [save_point, resting_point, storage_place]
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
    print("jakis exit z menu wypada zrobic(dodac do listy funkcje cofania? nazwac back to map?), np cofanie przed 'location'")
    return hero


def storage_place(hero, location):
    print("pokaż mi swoje towary")
    print("inventory gracza i storage do ktorego mozna odlozyc rzeczy")


def training_centre(hero, location):
    print("trenowanie jakiejś statystyki np STR za golda")


def store(hero, location):
    print("wejscie do sklepu gdzie mozna cos kupic i doda do inventory")


main()
