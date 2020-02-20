import shutil
import os
import controls
from termcolor import colored
import storage
import time
import sys


def config():
    columns = shutil.get_terminal_size().columns
    return columns


def welcome():
    os.system("clear")
    columns = config()
    title = '''
                                     _   _  _____  _      _     _  _____  _    _    _  _____ ______  _     ______ 
                                    | | | ||  ___|| |    | |   ( )|  _  |( )  | |  | ||  _  || ___ \| |    |  _  |
                                    | |_| || |__  | |    | |   |/ | | | ||/   | |  | || | | || |_/ /| |    | | | |
                                    |  _  ||  __| | |    | |      | | | |     | |/\| || | | ||    / | |    | | | |
                                    | | | || |___ | |____| |____  \ \_/ /     \  /\  /\ \_/ /| |\ \ | |____| |/ / 
                                    \_| |_/\____/ \_____/\_____/   \___/       \/  \/  \___/ \_| \_|\_____/|___/  
'''

    print(title)
    print("\n"*3)
    welcome = '''
                                A hundred years ago, the third world war took place, witch shook the foundations of the world. 
                            Causing disturbances at the space-time and spiritual level, opening the transition to a dimension
                            inhabited by dark forces. Phantoms and demons next to mutated humans and animals are wandering
                            around the world sowing annihilation for the few who survived. 
                            Magic stood next to science and a sword next to a machine gun.
                                A group of scientists and magicians created an extraordinary HERO.
                            Half human and half demon and robot, inhumanly strong, capable and resistand to magic. Only he
                            will be able to face the forces of evil and close the gates to hell.
                            That's YOU.
                                Traverse ravaged lands, defeat dark beasts, gather exparience, collect unique items and weapons
                            to finally defeat the prince of deamons and become a savior of men.

                                Let the adventure begin...'''
    # for char in welcome:
    #     if char == " ":
    #         sys.stdout.write(char)
    #         sys.stdout.flush()
    #         time.sleep(0.0)
    #     else:
    #         sys.stdout.write(char)
    #         sys.stdout.flush()
    #         time.sleep(0.02)
    print("\n" * 3)
    input("Press ENTER to continue".center(columns))


hair_one = """██████████████████████████████
█────────────────────────────█
█────────────────────────────█
█────────────────────────────█
█───────▄████████████▄───────█
█─────▄█░░░░░░░░░░░░░░█▄─────█
█───▄█░░░░░░░░░░░░░░░░░░█▄───█
█──▄█░░░░░░░░░░░░░░░░░░░░█▄──█"""

hair_two = """██████████████████████████████
█────────────────────────────█
█──█────██────██────██────█──█
█──██──████──████──████──██──█
█──████████████████████████──█
█──█████░░░░░░░░░░░░░░█████──█
█──███░░░░░░░░░░░░░░░░░░███──█
█──██░░░░░░░░░░░░░░░░░░░░██──█"""

hair_three = """██████████████████████████████
█────────────────────────────█
█──████████████████████████──█
█──████████████████████████──█
█──████████████████████████──█
█──█████░░░░░░░░░░░░░░█████──█
█──███░░░░░░░░░░░░░░░░░░███──█
█──██░░░░░░░░░░░░░░░░░░░░██──█"""

hair_four = """██████████████████████████████
█────────────────────────────█
█────────────────────────────█
█────────────────────────────█
█───────▄████████████▄───────█
█─────▄█░█░░█░░█░░█░░██▄─────█
█───▄██░░█░░█░░█░░█░░█░░█▄───█
█──▄█░█░░█░░█░░█░░█░░█░░██▄──█"""

eyes_one = """█──█░░░░░░░░░░░░░░░░░░░░░░█──█
█──█░░░██░░░░░░░░░░░░██░░░█──█
█──█░░░░░░░░░░░░░░░░░░░░░░█──█"""

eyes_two = """█──█░███████████████████░░█──█
█──█░▀████   ████    █▀░░░█──█
█──█░▀▄▄▄▄▄▀ ▀▄▄▄▄▄▀▀▀░░░░█──█"""

eyes_three = """█──█░░██▀▀███▄░░▄██▀▀███░░█──█
█──█░░██ ▀ ███░░███ ▀ ██░░█──█
█──█░░▀████▀░░░░░▀██████░░█──█"""

eyes_four = """█──█░░░░░░░░░░░░░░░░░░░░░░█──█
█──█░░░██████░░░░██████░░░█──█
█──█░░░░░░░░░░░░░░░░░░░░░░█──█"""

nose_one = """█──█░░░░░░░░░░░░░░░░░░░░░░█──█
█──█░░░░░░░░░░██░░░░░░░░░░█──█
█──█░░░░░░░░░░░░░░░░░░░░░░█──█"""

nose_two = """█──█░░░░░░░░░░██░░░░░░░░░░█──█
█──█░░░░░░░░░░███░░░░░░░░░█──█
█──█░░░░░░░░██████░░░░░░░░█──█"""

nose_three = """█──█░░░░░░░░░░░░░░░░░░░░░░█──█
█──█░░░░░░░░░░██░░░░░░░░░░█──█
█──█░░░░░░░░░@██@░░░░░░░░░█──█"""

nose_four = """█──█░░░░░░░░░░██░░░░░░░░░░█──█
█──█░░░░░░░░░@██@░░░░░░░░░█──█
█──█░░░░░░░░░░░░|░░░░░░░░░█──█"""

mouth_one = """█──█░░░░░░▄░░░░░░░░▄░░░░░░█──█
█──▀█░░░░░░▀██████▀░░░░░░█▀──█
█───▀█░░░░░░░░░░░░░░░░░░█▀───█"""

mouth_two = """█──█░░░░░░░░░░░░░░░░░░░░░░█──█
█──▀█░░░░░▄████████▄░░░░░█▀──█
█───▀█░░░░▀░░░░░░░░▀░░░░█▀───█"""

mouth_three = """█──█░░░░░░░░░░░░░░░░░░░░░░█──█
█──▀█░░░░░<========>░░░░░█▀──█
█───▀█░░░░░░░░░░░░░░░░░░█▀───█"""

mouth_four = """█──█░░░░░░░░░░░░░░░░░░░░░░█──█
█──▀█░░░░░░||||||||░░░░░░█▀──█
█───▀█░░░░░░░░░░░░░░░░░░█▀───█"""

beard_one = """█─────▀█░░░░░░░░░░░░░░█▀─────█
█───────▀████████████▀───────█
█────────────────────────────█
█────────────────────────────█
█────────────────────────────█
██████████████████████████████"""

beard_two = """█─────▀█░░░░░░░░░░░░░░█▀─────█
█───────▀████████████▀───────█
█───────────▀████▀───────────█
█─────────────██─────────────█
█────────────────────────────█
██████████████████████████████"""

beard_three = """█─────██░░░░░░░░░░░░░░██─────█
█─────██████████████████─────█
█─────██████████████████─────█
█─────██████████████████─────█
█────────────────────────────█
██████████████████████████████"""

beard_four = """█─────▀█░░░░░░░░░░░░░░█▀─────█
█───────▀████████████▀───────█
█─────────▀████████▀─────────█
█───────────▀████▀───────────█
█────────────────────────────█
██████████████████████████████"""


def printing_skull():
    columns = config()
    for x in range(7):
        print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM".center(columns))
        print("MMMMMMMMMMMM          MMMMMMMMMMMM".center(columns))
        print("MMMMMMMMMM              MMMMMMMMMM".center(columns))
        print("MMMMMMMMM                MMMMMMMMM".center(columns))
        print("MMMMMMMM                  MMMMMMMM".center(columns))
        print("MMMMMMM                   MMMMMMMM".center(columns))
        print("MMMMMMM                    MMMMMMM".center(columns))
        print("MMMMMMM                    MMMMMMM".center(columns))
        print("MMMMMMM    MMMM    MMMM    MMMMMMM".center(columns))
        print("MMMMMMM   MMMMMM   MMMMM   MMMMMMM".center(columns))
        print("MMMMMMM   MMMMMM   MMMMM   MMMMMMM".center(columns))
        print("MMMMMMMM   MMMMM M MMMMM  MMMMMMMM".center(columns))
        print("MMVKMMMM        MMM        MMMMMMM".center(columns))
        print("MMMMMMMM       MMMMM      MMMMMMMM".center(columns))
        print("MMMMMMMMMMMM   MMMMM  MMMMMMMMMMMM".center(columns))
        print("MMMMMMMMMM MMM       MM  MMMMMMMMM".center(columns))
        print("MMMMMMMMMM  M M M M M M MMMMMMMMMM".center(columns))
        print("MMMM  MMMMM MMMMMMMMMMM MMMMM   MM".center(columns))
        print("MMM    MMMM M MMMMMMM M MMMM    MM".center(columns))
        print("MMM    MMMM   M M M M  MMMMM   MMM".center(columns))
        print("MMMM    MMMM           MMM      MM".center(columns))
        print("MMM       MMMM       MMMM       MM".center(columns))
        print("MMM         MMMMMMMMMM      M  MMM".center(columns))
        print("MMMM  MMM      MMMMM      MMMMMMMM".center(columns))
        print("MMMMMMMMMMM  MM         MMMMMMM  M".center(columns))
        print("MMM  MMMMMMM         MMMMMMMMM   M".center(columns))
        print("MM    MMM        MMMM            M".center(columns))
        print("MM            MMMM              MM".center(columns))
        print("MMM        MMMMMMMMMMMMMMM       M".center(columns))
        print("MM      MMMMMMMMMMMMMMMMMMMMM    M".center(columns))
        print("MMM   MMMMMMMMMMMMMMMMMMMMMMMM   M".center(columns))
        print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM".center(columns))
        time.sleep(0.3)
        os.system("clear")
        print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM".center(columns))
        print("MMMMMMMMMMMM          MMMMMMMMMMMM".center(columns))
        print("MMMMMMMMMM              MMMMMMMMMM".center(columns))
        print("MMMMMMMMM                MMMMMMMMM".center(columns))
        print("MMMMMMMM                  MMMMMMMM".center(columns))
        print("MMMMMMM                   MMMMMMMM".center(columns))
        print("MMMMMMM                    MMMMMMM".center(columns))
        print("MMMMMMM                    MMMMMMM".center(columns))
        print("MMMMMMM    MMMM    MMMM    MMMMMMM".center(columns))
        print("MMMMMMM   MMMMMM   MMMMM   MMMMMMM".center(columns))
        print("MMMMMMM    MMMM    MMMM    MMMMMMM".center(columns))
        print("MMMMMMMM         M        MMMMMMMM".center(columns))
        print("MMVKMMMM        MMM        MMMMMMM".center(columns))
        print("MMMMMMMM       MMMMM      MMMMMMMM".center(columns))
        print("MMMMMMMMMMMM   MMMMM  MMMMMMMMMMMM".center(columns))
        print("MMMMMMMMMM  MM       MM  MMMMMMMMM".center(columns))
        print("MMMMMMMMMM    M M M M   MMMMMMMMMM".center(columns))
        print("MMMM  MMMMM  MMMMMMMMM  MMMMM   MM".center(columns))
        print("MMM    MMMM    MMMMM    MMMM    MM".center(columns))
        print("MMM    MMMM            MMMMM   MMM".center(columns))
        print("MMMM    MMMMMM       MMMMM      MM".center(columns))
        print("MMM       MMMMMMMMMMMMMMM       MM".center(columns))
        print("MMM         MMMMMMMMMM      M  MMM".center(columns))
        print("MMMM  MMM      MMMMM      MMMMMMMM".center(columns))
        print("MMMMMMMMMMM  MM         MMMMMMM  M".center(columns))
        print("MMM  MMMMMMM         MMMMMMMMM   M".center(columns))
        print("MM    MMM        MMMM            M".center(columns))
        print("MM            MMMM              MM".center(columns))
        print("MMM        MMMMMMMMMMMMMMM       M".center(columns))
        print("MM      MMMMMMMMMMMMMMMMMMMMM    M".center(columns))
        print("MMM   MMMMMMMMMMMMMMMMMMMMMMMM   M".center(columns))
        print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM".center(columns))
        time.sleep(0.3)
        os.system("clear")
    os.system("clear")


# def display_hero_avatar(face, style_list, cursor_position=0):
#     os.system("clear")
#     avatar_lst
#     face_element_name = ["Hair", "Eyes", "Nose", "Mouth", "Beard"]
#     # cursor_position = 0
#     print("WELCOME TO CHARACTER CREATOR\n")
#     print("'w'/'s' to move up/down")
#     print("'e' to change highlited element")
#     print("'x' to save your character")
#     for i in range(len(face)):
#         if cursor_position == i:
#             print(f"{face[i][style_list[i]]} Change: {colored((face_element_name[i]), 'red', 'on_grey', ['bold'])}")
#         else:
#             print(f"{face[i][style_list[i]]} Change: {face_element_name[i]}")

