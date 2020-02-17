import shutil
import os
from termcolor import colored


def config():
    columns = shutil.get_terminal_size().columns
    return columns


def welcome():
    os.system("clear")
    print("WELCOME TO DA GAME")
    input()


def display_distribute_stats(spare_points, character, cursor_position=0):
    os.system("clear")
    columns = config()
    stats_names = ["STR", "CON", "DEX", "INT"]
    spare_points = colored((spare_points), 'red', "on_grey", ["bold"])
    print(f"You have {spare_points} to assign. Choose wisely.".center(columns+18))
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


def print_map(x, y, player_position):
    POSITION_X = 0
    POSITION_Y = 1
    os.system('clear')
    map = ''
    for i in range(x):
        for j in range(y):
            if i == 0 or i == x - 1 or j == 0 or j == y - 1:
                map += '#'
            else:
                if player_position[POSITION_X] == i and player_position[POSITION_Y] == j:
                    map += '@'
                else:
                    map += '.'

        map += '\n'
    print(map)
