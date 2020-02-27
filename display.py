import shutil
import os
from termcolor import colored
import time
import storage
import ascii_art
import controls
import engine


def config():
    columns = shutil.get_terminal_size().columns
    return columns


def print_message(message, wait=True, press_any_key=True):
    columns = config()
    print()
    print(message.center(columns))
    if wait:
        input((int(config()/2)) * " ")
    elif press_any_key:
        print("Type in any key to continue.".center(columns))
        input((int(config()/2)) * " ")

# def display_no_wormhole_keys():
#     columns = config()
#     print("You don't have any priveleaged keys, get out of my way!".center(columns))
#     input()


def print_map(map, hero_position, dark=False, sight=5):
    os.system('clear')
    field = []
    for i in range(len(map)):
        line = ""
        for j in range(len(map[i])):
            if check_sight(sight, [hero_position[0], hero_position[1]], [i, j]):
                if i == hero_position[0] and j == hero_position[1]:
                    line += '@'
                else:
                    line += colored((map[i][j]['symbol']), map[i][j]['color'], 'on_grey', ['bold'])
            else:
                line += ' '
        field.append(line)
    field.append("You are now walking on " + map[hero_position[0]][hero_position[1]]['name'])
    return field


def check_sight(sight, hero_position, place):
    if all([abs(hero_position[0]-place[0]) <= sight, abs(hero_position[1]-place[1]) <= sight]):
        return True
    else:
        return False


def npc_message(npc_message, hero_name, npc_name):
    columns = config()
    upper = [" ", (f'Mightfull {hero_name}, you met {npc_name} on your way to glory, listen carefuly:'), " "]
    left = storage.load_avatar_from_file(hero_name)
    right = storage.load_avatar_from_file(npc_name)
    lower = [" "]
    if len(npc_message) > columns - 10:
        npc_message_1 = npc_message.split()
        words_in_line = len(npc_message_1) // 2
        line1 = []
        line2 = []
        for x, word in enumerate(npc_message_1):
            if x < words_in_line:
                line1.append(word)
            else:
                line2.append(word)
        lower.append(" ".join(line1))
        lower.append(" ".join(line2))
    else:
        lower.append(npc_message)
    main_display(upper, lower, left, right)
    input()


def display_avatar():
    pass


def main_display(upper, lower, left=[""], right=[""], right_length=30, left_length=30):
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
        a = len(repr(line))
        if a > 36:
            print(line.center(columns+18))
        else:
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


def display_menu(title, options_list, cursor_position=0, extras="", extras_2=""):
    lower_display = []
    lower_display.append(title)
    lower_display.append(extras)
    for i in range(len(options_list)):
        if cursor_position == i:
            lower_display.append(f"{colored((options_list[i]), 'red', 'on_grey', ['bold'])}")
        else:
            lower_display.append(f"{options_list[i]}")
    lower_display.append(extras_2)
    return lower_display


def display_location_menu(location, locations_functions, cursor_position=0):
    os.system("clear")
    columns = config()
    welcome_message = f"Welcome to {location['name']}! Take your time\n"
    print(welcome_message.center(columns))
    for i in range(len(locations_functions)):
        if cursor_position == i:
            print(f"{colored((str(locations_functions[i])), 'red', 'on_grey', ['bold'])}".center(columns+18))
        else:
            print(f"{str(locations_functions[i])}".center(columns))


def display_fight_mode(hero, enemy):
    s1 = f"YOUR HP: {round(hero['hp'])}"
    s2 = f"ENEMY'S HP: {round(enemy['hp'])}"
    return s1, s2


def missed_attack(attacker_name):
    print(f"{attacker_name} missed!")


def taken_damage_print(attacker_name, damage_taken):
    return f"{attacker_name} took {damage_taken}"


def display_stats(hero):
    lvl = engine.calculate_hero_lvl(hero)
    line_0 = f"LVL:\t {lvl}"
    line_1 = f"Name: {hero['name']}\t STR: {hero['STR']}"
    line_2 = f"Experience: {hero['exp']}\t CON: {hero['CON']}"
    line_3 = f"Hit Points: {int(hero['hp'])}\t DEX: {hero['DEX']}"
    line_4 = f"Position: {hero['position']}\t INT: {hero['INT']}"
    concatenated_stats = [line_0, line_1, line_2, line_3, line_4]
    return concatenated_stats


def display_lose_game():
    ascii_art.printing_skull()
    exit()


def print_blank_screen():
    os.system('clear')
    print("██"*1800)
    time.sleep(0.05)


def display_hero_avatar(face, style_list, cursor_position=0):
    os.system("clear")
    face_element_name = ["Hair", "Eyes", "Nose", "Mouth", "Beard"]
    face_lines_list = []
    header = [" "]
    header.append("WELCOME TO CHARACTER CREATOR\n")
    header.append("'w'/'s' to move up/down")
    header.append("'e' to change highlited element")
    header.append("'x' to save your character\n")
    for i in range(len(face)):
        face_part = face[i][style_list[i]].split("\n")
        face_lines_list.extend(face_part)
    menu_lines = [" ", " ", " ", " "]
    for i in range(len(face)):
        if cursor_position == i:
            menu_lines.append(colored((face_element_name[i]), 'red', 'on_grey', ['bold']))
            menu_lines.append(" ")
            menu_lines.append(" ")
        else:
            menu_lines.append(face_element_name[i])
            menu_lines.append(" ")
            menu_lines.append(" ")
    return header, face_lines_list, menu_lines


def create_hero_avatar(hero_name):
    hero_hair = [ascii_art.hair_one, ascii_art.hair_two, ascii_art.hair_three, ascii_art.hair_four]
    hero_eyes = [ascii_art.eyes_one, ascii_art.eyes_two, ascii_art.eyes_three, ascii_art.eyes_four]
    hero_nose = [ascii_art.nose_one, ascii_art.nose_two, ascii_art.nose_three, ascii_art.nose_four]
    hero_mouth = [ascii_art.mouth_one, ascii_art.mouth_two, ascii_art.mouth_three, ascii_art.mouth_four]
    hero_beard = [ascii_art.beard_one, ascii_art.beard_two, ascii_art.beard_three, ascii_art.beard_four]
    hair_style = 0
    eyes_style = 0
    nose_style = 0
    mouth_style = 0
    beard_style = 0
    cursor_position = 0
    user_key = None
    style_list = [hair_style, eyes_style, nose_style, mouth_style, beard_style]
    face = [hero_hair, hero_eyes, hero_nose, hero_mouth, hero_beard]
    main_display(display_hero_avatar(face, style_list, cursor_position)[0], [""],
                 left=display_hero_avatar(face, style_list, cursor_position)[1],
                 right=display_hero_avatar(face, style_list, cursor_position)[2])
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
            hero_face = [hero_hair[style_list[0]], hero_eyes[style_list[1]], hero_nose[style_list[2]],
                         hero_mouth[style_list[3]], hero_beard[style_list[4]]]
            string_hero_face = "\n".join(hero_face)
            hero_avatar_to_print = string_hero_face.split("\n")
            hero_avatar_to_print = [list(element) for element in hero_avatar_to_print]
            return hero_face
        main_display(display_hero_avatar(face, style_list, cursor_position)[0], [""],
                     left=display_hero_avatar(face, style_list, cursor_position)[1],
                     right=display_hero_avatar(face, style_list, cursor_position)[2])


def beaten_face(avatar):
    pass
