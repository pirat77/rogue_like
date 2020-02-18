import controls
import os
import display
import common_functions
import storage
from termcolor import colored


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
    hero["hp"] = 100
    hero["name"] = input("Enter a name: ")
    valid_name = storage.check_for_existing_name(hero["name"], "saves")
    while not valid_name:
        hero["name"] = input("User name already exist, type another name: ")
        valid_name = storage.check_for_existing_name(hero["name"], "saves")
    hero["stats"] = common_functions.distribute_stat_points()
    hero["inv"] = {}
    hero["position"] = [3, 45]
    print(hero)
    storage.save_to_file(hero)
    # hero_full_info = [hero_name, hero_stats, hero_hp, hero_exp, "", "forest", [3, 45]]
    game_play(hero, common_functions.load_map("forest"))


def load_game():
    user_name = input("What character do you want to load? Type hero's name: ")
    if storage.check_for_existing_name(user_name):
        display.print_hero_not_found()
    else:
        raw_data = storage.load_from_file(user_name)
        print(raw_data)


def about():
    print("about")


def explore_menu():
    cursor_position = 0
    options_functions = [new_game, load_game, about, exit]
    display.display_start_menu()
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
        display.display_start_menu(cursor_position)


def main():
    display.welcome()
    explore_menu()


def game_play(hero, map):
    map_size = [len(map), len(map[0])]
    hero_position = hero["position"]
    in_menu = False
    while not in_menu:
        display.print_map(map, hero_position)
        previous_position_y, previous_position_x = hero_position[0], hero_position[1]
        hero_position, in_menu = common_functions.moving_on_map(map_size, hero_position)
        field_type = map[hero_position[0]][hero_position[1]]['type']
        if field_type == 'terrain':
            if map[hero_position[0]][hero_position[1]]['can_enter?'] == 'N':
                hero_position = [previous_position_y, previous_position_x]

        elif field_type == 'enemy':
            fight_mode(hero, map[hero_position[0]][hero_position[1]])

        elif field_type == 'door':
            enter_portal(hero, map[hero_position[0]][hero_position[1]])


def enter_portal(hero, door):
    if int(hero["exp"]) < int(door['exp_needed']):
        display.print_more_exp_needed(door['exp_needed'])
        return 0
    if door['key_needed'] == "":
        hero["position"] = [int(door['hero_position_y']), int(door['hero_position_x'])]
        game_play(hero, common_functions.load_map(door['heading_to']))


def fight_mode(hero, enemy):
    print(str(hero))
    print(str(enemy))
    input()


main()
