import shutil
import os
from termcolor import colored


def config():
    columns = shutil.get_terminal_size().columns
    return columns


def print_map(map, hero_position):
    os.system('clear')
    for i in range(len(map)):
        for j in range(len(map[i])):
            if i == hero_position[0] and j == hero_position[1]:
                print('@', end='') 
            else:
                print(colored((map[i][j]['symbol']), map[i][j]['color'], 'on_grey', ['bold']), end='')
        print('')


def welcome():
    os.system("clear")
    print("WELCOME TO DA GAME")
    input()


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


def display_start_menu(cursor_position=0):
    os.system("clear")
    columns = config()
    options_names = ["NEW GAME", "LOAD GAME", "ABOUT", "EXIT"]
    print("MAIN MENU".center(columns))
    print()
    for i in range(len(options_names)):
        if cursor_position == i:
            print(f"{colored((options_names[i]), 'red', 'on_grey', ['bold'])}".center(columns+18))
        else:
            print(f"{options_names[i]}".center(columns))


def print_hero_not_found():
    print("Hero was not found.")
    input("Press any key to continue.")


def print_more_exp_needed(exp_needed):
    print(f"You need {exp_needed} exp to enter this portal.")
    input("Press any key to continue.")
