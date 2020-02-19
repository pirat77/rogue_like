import shutil
import os
from termcolor import colored
import time
import sys


def config():
    columns = shutil.get_terminal_size().columns
    return columns


def print_map(map, hero_position, hero_avatar=""):
    os.system('clear')
    # print(hero_avatar)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if i == hero_position[0] and j == hero_position[1]:
                print('@', end='')
            else:
                print(colored((map[i][j]['symbol']), map[i][j]['color'], 'on_grey', ['bold']), end='')
        print('')
    print("You are now walking on " + map[hero_position[0]][hero_position[1]]['name'])


def display_distribute_stats(spare_points, character, cursor_position=0):
    os.system("clear")
    columns = config()
    stats_names = ["STR", "CON", "DEX", "INT"]
    spare_points = colored((spare_points), 'red', "on_grey", ["bold"])
    print(f"You have {spare_points} points to assign. Choose wisely.".center(columns+18))
    for i in range(len(stats_names)):
        if cursor_position == i:
            print(f"{stats_names[i]} : {colored((character[stats_names[i]]), 'red', 'on_grey', ['bold'])}".center(columns+18))
        else:
            print(f"{stats_names[i]} : {character[stats_names[i]]}".center(columns))


# def display_start_menu(cursor_position=0):
#     os.system("clear")
#     columns = config()
#     options_names = ["NEW GAME", "LOAD GAME", "ABOUT", "EXIT"]
#     print("MAIN MENU".center(columns))
#     print()
#     for i in range(len(options_names)):
#         if cursor_position == i:
#             print(f"{colored((options_names[i]), 'red', 'on_grey', ['bold'])}".center(columns+18))
#         else:
#             print(f"{options_names[i]}".center(columns))


def display_menu(title, options_list, cursor_position=0, extras="", extras_2=""):
    os.system("clear")
    columns = config()
    print(title.center(columns))
    print(extras.center(columns))
    for i in range(len(options_list)):
        if cursor_position == i:
            print(f"{colored((options_list[i]), 'red', 'on_grey', ['bold'])}".center(columns+18))
        else:
            print(f"{options_list[i]}".center(columns))
    print(extras_2.center(columns))


def print_hero_not_found():
    print("Hero was not found.")
    input("Press any key to continue.")


def print_more_exp_needed(exp_needed):
    print(f"You need {exp_needed} exp to enter this portal.")
    input("Press any key to continue.")


def display_location_menu(location, locations_functions, cursor_position=0):
    os.system("clear")
    columns = config()
    welcome_message = f"Welcome to {location['name']}! Take your time"
    # options_names = ["SAVE GAME", "HEAL", "ENTER STORAGE"] -> może location functions(liste) przerobic na słownik
    print(welcome_message.center(columns))
    print()
    for i in range(len(locations_functions)):
        if cursor_position == i:
            print(f"{colored((locations_functions[i]), 'red', 'on_grey', ['bold'])}".center(columns+18))
        else:
            print(f"{locations_functions[i]}".center(columns))


def display_fight_mode(hero, enemy):
    os.system("clear")
    columns = config()
    s1 = f"YOUR HP: {round(hero['hp'])}".center(columns)
    s2 = f"YOUR ENEMY'S HP: {round(enemy['hp'])}".center(columns)
    return s1 + "\n" + s2 + "\n"


def missed_attack(attacker_name):
    print(f"{attacker_name} missed!")
    input()


def taken_damage_print(attacker_name, damage_taken):
    return f"{attacker_name} took {damage_taken}"
    