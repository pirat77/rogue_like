import display
import storage
import ascii_art
import engine
import events


def new_game():
    columns = display.config()
    hero = {}
    display.print_message("Enter a name: ", False, False)
    hero["name"] = input((int(columns/2)) * " ")
    valid_name = storage.check_for_existing_name(hero["name"], "saves")
    while not valid_name:
        hero["name"] = input("User name already exist, type another name: ")
        valid_name = storage.check_for_existing_name(hero["name"], "saves")
    storage.save_avatar_to_file(hero["name"], display.create_hero_avatar(hero["name"]))
    hero.update(engine.distribute_stat_points())
    hero = hero_set_up(hero)
    storage.save_to_file(hero)
    game_play(hero, engine.load_map("city")[0], engine.load_map("city")[1])


def hero_set_up(hero):
    hero["exp"] = 1
    hp_for_one_STR_point = 3
    hp_for_one_CON_point = 10
    hero_max_hp = hero['STR'] * hp_for_one_STR_point + hero['CON'] * hp_for_one_CON_point
    hero["hp"] = hero_max_hp
    hero["inv"] = {}
    hero["position"] = [10, 10]
    hero["map"] = "city"
    hero["weapon_on"] = ""
    hero["armor_on"] = ""
    hero["amulet_on"] = ""
    return hero


def load_game():
    display.print_message("What character do you want to load? Type hero's name: ", wait=False, press_any_key=False)
    user_name = input((int(display.config()/2)) * " ")
    if storage.check_for_existing_name(user_name, "saves"):
        display.print_message("Hero not found.", False, True)
        main(False)
    else:
        hero = eval(storage.load_from_file(user_name))
        game_play(hero, engine.load_map(hero["map"])[0], engine.load_map("city")[1])


def about(in_game_already):
    upper = ['', '', 'Good Luck']
    lower = [' ', ' ', 'Welcome to Hell\'O\' Word',
             'This game has been created', 'in three days,',
             'by top_level team of hackers',
             'from NSA', 'Your objective is simple:',
             'You have to save the word',
             'Kill monsters, love widows,',
             'gather gold,',
             'explore dungeons',
             'Game controls are as easy',
             'as it can be:', 'w - go north',
             's - go south',
             'a - go east',
             'd - go west',
             '+ - accept options in menu',
             'follow instructions on the screen']
    display.main_display(upper, lower)
    input()
    explore_menu(in_game_already)


def explore_menu(in_game_already=True, hero={}):
    cursor_position = 0
    title = "MAIN MENU"
    options_functions = [new_game, load_game, about, exit]
    options_display = {new_game: "NEW GAME", load_game: "LOAD GAME", about: "ABOUT", exit: "EXIT"}
    if in_game_already:
        options_functions.insert(0, resume)
        options_functions.insert(0, engine.inventory)
        options_display.update({resume: "RESUME", engine.inventory: "INVENTORY"})
    function_list_lenght = len(options_functions)
    user_key = False
    options_names = [options_display[x] for x in options_functions]
    while not user_key:
        display_menu = display.display_menu(title, options_names, cursor_position)
        display.main_display([""], lower=display_menu)
        cursor_position, user_key = engine.navigating_menus(function_list_lenght, cursor_position)
    try:
        options_functions[cursor_position]()
    except TypeError:
        if cursor_position == 0:
            options_functions[cursor_position](hero)
        else:
            options_functions[cursor_position](in_game_already)


def main(show_welcome=True):
    if show_welcome:
        ascii_art.welcome()
    explore_menu(False)


def resume(in_game_already):
    return in_game_already


def game_play(hero, map, map_name):
    # TODO: comming clowser, flash only hited, blood, shooting
    map_size = [len(map), len(map[0])]
    hero_avatar = storage.load_avatar_from_file(hero["name"])
    upper_title = ["\n", f"{hero['name']}, you are now exploring {map_name}.", ""]
    in_menu = False
    while not in_menu:
        if hero['map'] != map_name:
            map = engine.load_map(hero['map'])[0]
            map_name = hero['map']
        display.main_display(upper_title, left=hero_avatar, right=display.print_map(map, hero['position']),
                             lower=display.display_stats(hero), right_length=map_size[1])
        previous_position_y, previous_position_x = int(hero["position"][0]), int(hero["position"][1])
        hero["position"], in_menu = engine.moving_on_map(map_size, hero["position"])
        if in_menu:
            in_menu = explore_menu(True, hero)
        field_type = map[hero["position"][0]][hero["position"][1]]['type']
        if field_type == 'terrain':
            if map[hero["position"][0]][hero["position"][1]]['can_enter?'] == 'N':
                hero["position"] = [previous_position_y, previous_position_x]
        elif field_type == 'enemy':
            events.fight_mode(hero, map[hero["position"][0]][hero["position"][1]])
        elif field_type == 'door':
            events.enter_portal(hero, map[hero["position"][0]][hero["position"][1]])
        elif field_type == 'location':
            events.location_menu(hero, map[hero["position"][0]][hero["position"][1]])
        elif field_type == 'npc':
            events.encounter(hero, map[hero["position"][0]][hero["position"][1]])
        elif field_type == 'item':
            events.add_item_to_inventory(hero, map[hero['position'][0]][hero['position'][1]])


main()
