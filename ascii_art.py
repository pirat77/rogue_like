import shutil
import os
import controls
from termcolor import colored

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

eyes_three = """█──█░░██▀▀███▄  ▄██▀▀███░░█──█
█──█░░██ ▀ ███  ███ ▀ ██░░█──█
█──█░░▀████▀     ▀██████░░█──█"""

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


def display_hero_avatar(face, style_list, cursor_position=0):
    os.system("clear")
    face_element_name = ["Hair", "Eyes", "Nose", "Mouth", "Beard"]
    # cursor_position = 0
    print("WELCOME TO CHARACTER CREATOR!!!\n")
    print("Press 'w'/'s' to move up/down\n")
    print("Press 'e' to change highlited element\n")
    print("When you finished, press 'x' to save your character\n")
    for i in range(len(face)):
        if cursor_position == i:
            print(f"{face[i][style_list[i]]} Change: {colored((face_element_name[i]), 'red', 'on_grey', ['bold'])}")
        else:
            print(f"{face[i][style_list[i]]} Change: {face_element_name[i]}")


def create_hero_avatar():

    hero_hair = [hair_one, hair_two, hair_three, hair_four]
    hero_eyes = [eyes_one, eyes_two, eyes_three, eyes_four]
    hero_nose = [nose_one, nose_two, nose_three, nose_four]
    hero_mouth = [mouth_one, mouth_two, mouth_three, mouth_four]
    hero_beard = [beard_one, beard_two, beard_three, beard_four]

    hair_style = 0
    eyes_style = 0
    nose_style = 0
    mouth_style = 0
    beard_style = 0

    cursor_position = 0
    user_key = None
    style_list = [hair_style, eyes_style, nose_style, mouth_style, beard_style]
    face = [hero_hair, hero_eyes, hero_nose, hero_mouth, hero_beard]
    display_hero_avatar(face, style_list, cursor_position)

    while user_key != "x":
        user_key = controls.getch()
        if user_key == "s" and cursor_position < 4:
            cursor_position += 1
        elif user_key == "w" and cursor_position > 0:
            cursor_position -= 1
        elif user_key == "e":
            if style_list[cursor_position] < len(face[cursor_position])-1:
                style_list[cursor_position] += 1
            else:
                style_list[cursor_position] = 0
        elif user_key == "x":
            hero_face = [hero_hair[style_list[0]], hero_eyes[style_list[1]], hero_nose[style_list[2]], hero_mouth[style_list[3]], hero_beard[style_list[4]]]
            string_hero_face = "\n".join(hero_face)
            # print(string_hero_face)
            hero_avatar_to_print = string_hero_face.split("\n")
            # print(hero_avatar_to_print)
            return hero_face, hero_avatar_to_print
        display_hero_avatar(face, style_list, cursor_position)

