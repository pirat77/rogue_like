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


hero = {"STR": 10, "CON": 10, "DEX": 10, "INT": 10}


print(display_distribute_stats(spare_points=10, character=hero))
