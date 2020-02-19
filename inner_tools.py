import sys
import controls
from termcolor import colored
import common_functions
import storage
import os


PATH = sys.argv[0].strip("inner_tools.py") + "game_data/"


def print_map(map, hero_position):
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


def object_creator():
    which_map = input("Which map's object are you editing?")
    available_color = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'no_color']
    object_types = ['item', 'npc', 'enemy', 'riddle', 'terrain', 'door', 'location']
    item_usage_types = ["weapon", "armor", "amulet", "food", "key", "gold"]
    object_questionaries = {'item': ['weight', 'dmg+', 'hp+', 'deffence+', 'agility+', "used_for"],
                            'enemy': ["STR", "CON", "DEX", "INT", "hp", "agility+", "deffence+", "dmg+", "item", "exp+"],
                            "npc": ["welcome_message", "condition", "special_message", "item", "exp+"],
                            "door": ["heading_to", "hero_position_x", "hero_position_y", "key_needed", "exp_needed"],
                            "riddle": ["question", "answer", "exp+", "bad_answer_message", "good_answer_message", "item"],
                            "terrain": ['can_enter?'],
                            "location": ['save_point', 'resting_point', 'storage_place', 'store', 'training_centre']}
    game_piece = {'symbol': '', 'color': '', 'type': ''}
    game_piece['name'] = input("What is the name of object?: ")
    while len(game_piece['symbol']) != 1:
        game_piece['symbol'] = input("Enter object symbol (one char): ")
    while game_piece['color'] not in available_color:
        game_piece['color'] = input("Enter object color: " + str(available_color) + ' ')
    while game_piece['type'] not in object_types:
        game_piece['type'] = input("Enter object type: " + str(object_types) + ' ')
    for question in object_questionaries[game_piece['type']]:
        if question == "used_for":
            print(item_usage_types)
        game_piece[question] = input("Enter " + question + " of object: ")    
    with open(PATH + which_map + '.txt', "a") as f:
        f.write(str(game_piece)+"\n")
    print(str(game_piece) + " printed to file.")
    if_exit = input("If you want another one? Press enter, else type exit ")
    if if_exit != "exit":
        object_creator()
    else:
        print("See ya later, man.")


def load_map(map_name):
    with open(str(PATH + map_name + ".lvl"), "r") as f:
        map_string = f.read()
        map = eval(map_string)
    return map


def map_editor():
    hero_position = [0, 0]
    map_name = input("Enter level name: ")
    game_pieces_list = load_gamepieces(map_name)    
    try:
        map = load_map(map_name)
    except FileNotFoundError:
        map = generate_new_map()

    map_size = [len(map), len(map[0])]

    while True:
        print_map(map, hero_position)
        for x, element in enumerate(game_pieces_list):
            print(f"{x} {colored(element['symbol'], element['color'], 'on_grey', ['bold'])} {element['type']} {element['name']}")
        print("Move WSAD, add object +")
        hero_position, if_action = common_functions.moving_on_map(map_size, hero_position)
        if if_action:
            selected_option = input('Enter id of object to add it on your postion (666 - save and exit, 77 - smudge)')
            if selected_option == '666':
                break
            if selected_option == "77":
                pen = input("Which object do you want to draw with?")
                if_action = False
                while not if_action:
                    print_map(map, hero_position)
                    print(f"Symbol you are drawing with is: {game_pieces_list[int(pen)]['symbol']}")
                    hero_position, if_action = common_functions.moving_on_map(map_size, hero_position)
                    map[hero_position[0]][hero_position[1]] = game_pieces_list[int(pen)]
                selected_option = pen
            map[hero_position[0]][hero_position[1]] = game_pieces_list[int(selected_option)]
    print('map gonna be saved here, waiting for ya, cya')
    with open(str(PATH + map_name + ".lvl"), "w") as f:
        f.write(str(map))


def generate_new_map():
    map = []
    lvl_i = int(input('It is a new map, enter it\'s lenght: '))
    lvl_j = int(input('Enter is height: '))
    for j in range(lvl_j):
        map_line = []
        for i in range(lvl_i):
            map_line.append({'symbol': '.', 'color': 'white', 'type': 'terrain', 'name': 'Empty space', 'can_enter?': 'Y'})
        map.append(map_line)
    return map


def load_gamepieces(which_map):
    game_pieces_list = []
    with open(PATH + which_map + '.txt', "r") as f:
        game_pieces = f.readlines()
    for element in game_pieces:
        game_pieces_list.append(eval(element))
    game_pieces_list = sorted(game_pieces_list, key=lambda k: k['type'])
    return game_pieces_list


def main():
    mode = input('Hi, dev. What you gonna do? objects or maps, huh? ')  
    if mode == 'objects':
        object_creator()
    elif mode == 'maps':
        map_editor()
    else:
        print('no mode selected, go home! ')


main()


