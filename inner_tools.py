import sys
from display import print_map

def object_creator():
    available_color = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'black']
    object_types = ['item', 'npc', 'enemy', 'riddle', 'terrain', 'door', 'location']
    object_questionaries = {'item': ['weight', 'atk+', 'hp+', 'deffence+', 'dodge+', 'aiming+'], 'enemy': ["STR", "CON", "DEX", "INT", "hp", "aiming+", "dodge+", "deffence+", "atk+", "item", "exp+"], "door": ["heading_to", "key_needed", "exp_needed"], "riddle": ["question", "answer", "exp+", "bad_answer_message", "good_answer_message", "item"], "terrain": ['can_enter?']}
    game_piece = {'symbol': '', 'color': '', 'type': ''}
    game_piece['name'] = input("What is the name of object?: ")
    while len(game_piece['symbol']) != 1:
        game_piece['symbol'] = input("Enter object symbol (one char): ")
    while game_piece['color'] not in available_color:
        game_piece['color'] = input("Enter object color: " + str(available_color) + ' ')
    while game_piece['type'] not in object_types:
        game_piece['type'] = input("Enter object type: " + str(object_types) + ' ')
    for question in object_questionaries[game_piece['type']]:
        game_piece[question] = input("Enter " + question + " of object: ")
    with open('game_pieces.txt', "a") as f:
        f.write(str(game_piece)+"\n")
    print(str(game_piece) + " printed to file.")
    if_exit = input("If you want another one? Press enter, else type exit ")
    if if_exit != "exit":
        object_creator()
    else:
        print("See ya later, man.")


def main():
    map = [[{'symbol': '|', 'color': 'magenta', 'type': 'door', 'name': 'Portal', 'heading_to': 'city_in_clouds', 'key_needed': 'silver_trumpet', 'exp_needed': '350'}, {'symbol': '.', 'color': 'white', 'type': 'terrain', 'name': 'Empty space', 'can_enter?': 'Y'}, {'symbol': '.', 'color': 'white', 'type': 'terrain', 'name': 'Empty space', 'can_enter?': 'Y'}], [{'symbol': '|', 'color': 'magenta', 'type': 'door', 'name': 'Portal', 'heading_to': 'city_in_clouds', 'key_needed': 'silver_trumpet', 'exp_needed': '350'}, {'symbol': '.', 'color': 'white', 'type': 'terrain', 'name': 'Empty space', 'can_enter?': 'Y'}, {'symbol': '.', 'color': 'white', 'type': 'terrain', 'name': 'Empty space', 'can_enter?': 'Y'}], [{'symbol': '|', 'color': 'magenta', 'type': 'door', 'name': 'Portal', 'heading_to': 'city_in_clouds', 'key_needed': 'silver_trumpet', 'exp_needed': '350'}, {'symbol': '.', 'color': 'white', 'type': 'terrain', 'name': 'Empty space', 'can_enter?': 'Y'}, {'symbol': '.', 'color': 'white', 'type': 'terrain', 'name': 'Empty space', 'can_enter?': 'Y'}]]
    print_map(map)

main()