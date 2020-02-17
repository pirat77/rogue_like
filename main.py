import controls
import os
import display
import common_functions
import storage


def new_game():
    os.system("clear")
    # face configuration
    hero_exp = 1
    hero_hp = 100
    hero_name = input("Enter a name: ")
    valid_name = storage.check_for_existing_name(hero_name)
    while not valid_name:
        hero_name = input("User name already exist, type another name: ")
        valid_name = storage.check_for_existing_name(hero_name)
    hero_stats = common_functions.distribute_stat_points()
    storage.save_to_file(hero_name, hero_stats, hero_hp, hero_exp)


def load_game():
    user_name = input("What character do you want to load? Type hero's name: ")
    if storage.check_for_existing_name(user_name):
        display.print_hero_not_found()
    else:
        raw_data = storage.load_from_file(user_name)
        hero_info = raw_data.split("|")[0]
        inventory = raw_data.split("|")[1]
        hero_name = hero_info[0]
        hero_stats = hero_info[1:5]
        hero_hp = hero_info[5]
        hero_exp = hero_info[6]
        print(raw_data)


def about():
    print("about")


def explore_menu():
    cursor_position = 0
    # options_names = ["NEW GAME", "LOAD GAME", "ABOUT", "EXIT"]
    options_functions = [new_game, load_game, about, exit]
    display.display_start_menu()
    user_key = None
    while user_key != "+":
        user_key = controls.getch()
        if user_key == "s" and cursor_position < 3:
            cursor_position += 1
        elif user_key == "w" and cursor_position > 0:
            cursor_position -= 1
        elif user_key == "+":
            options_functions[cursor_position]()
            break
        display.display_start_menu(cursor_position)


def main():
    display.welcome()
    explore_menu()


main()
