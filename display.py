import shutil
import os
from termcolor import colored
import time
import sys
import storage


def config():
    columns = shutil.get_terminal_size().columns
    return columns


def print_map(map, hero_position):
    os.system('clear')
    field = []
    for i in range(len(map)):
        line = ""
        for j in range(len(map[i])):
            if i == hero_position[0] and j == hero_position[1]:
                line += '@'
            else:
                line += colored((map[i][j]['symbol']), map[i][j]['color'], 'on_grey', ['bold'])
        field.append(line)
    field.append("You are now walking on " + map[hero_position[0]][hero_position[1]]['name'])
    return field


def npc_message(npc_message, hero_name, npc_name):
    upper = (f'Mightfull {hero_name}, you met {npc_name} on your way to glory, listen carefuly:')
    left = storage.load_avatar_from_file(hero_name)
    right = storage.load_avatar_from_file(npc_name)
    lower = npc_message
    main_display(upper, left, right, lower)


def display_avatar():
    pass


def main_display(upper, left, right, lower, right_length=30, left_length=30):
    os.system('clear')
    columns = config()
    for line in upper:
        print(line.center(columns))
    spread = " " * 20
    left_spread = " " * int((columns/2) - 10 - left_length)
    for i in range(min(len(left), len(right))):
        print(f"{left_spread}{left[i]}{spread}{right[i]}")
    last_lines = len(left) - len(right)
    if last_lines > 0:
        for element in left[len(left) - last_lines::]:
            print(f"{left_spread}{element}")
    elif last_lines < 0:
        left_spread += " " * len(left[0])
        for element in right[len(right) - last_lines::]:
            print(f"{left_spread}{element}")
    for line in lower:
        print(line.center(columns))


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
    lower_display = ""
    lower_display += title + "\n"
    lower_display += extras + "\n"
    for i in range(len(options_list)):
        if cursor_position == i:
            lower_display += f"{colored((options_list[i]), 'red', 'on_grey', ['bold'])}\n"
        else:
            lower_display += f"{options_list[i]}\n"
    lower_display += extras_2
    return lower_display


def print_hero_not_found():
    print("Hero was not found.")
    input("Press any key to continue.")


def print_more_exp_needed(exp_needed):
    print(f"You need {exp_needed} exp to enter this portal.")
    input("Press any key to continue.")


def display_location_menu(location, locations_functions, cursor_position=0):
    os.system("clear")
    columns = config()
    welcome_message = f"Welcome to {location['name']}! Take your time\n"
    # options_names = ["SAVE GAME", "HEAL", "ENTER STORAGE"] -> może location functions(liste) przerobic na słownik
    print(welcome_message.center(columns))
    for i in range(len(locations_functions)):
        if cursor_position == i:
            print(f"{colored((str(locations_functions[i])), 'red', 'on_grey', ['bold'])}".center(columns+18))
        else:
            print(f"{str(locations_functions[i])}".center(columns))


def display_fight_mode(hero, enemy):
    s1 = f"YOUR HP: {round(hero['hp'])}"
    s2 = f"YOUR ENEMY'S HP: {round(enemy['hp'])}"
    return s1 + "\n" + s2 + "\n"


def missed_attack(attacker_name):
    print(f"{attacker_name} missed!")
    input()


def taken_damage_print(attacker_name, damage_taken):
    return f"{attacker_name} took {damage_taken}"


def display_stats(hero):
    print(f"Name: {hero['name']}\t STR: {hero['STR']}")
    print(f"Experience: {hero['exp']}\t CON: {hero['CON']}")
    print(f"Current Map: {hero['map']}\t DEX: {hero['DEX']}")
    print(f"Position: {hero['position']}\t INT: {hero['INT']}")

    
def display_lose_game():
    print("YOU DIE")
    
