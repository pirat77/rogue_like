import display
import controls


def new_game():
    print("new game")


def load_game():
    print("load game")


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


def moving_on_map():
    DIRRECTIONS = {'w': [-1, 0], 's': [1, 0], 'a': [0, -1], 'd': [0, 1]}
    player_position = [3, 3]
    MAP_SIZE = [15, 15]
    life = 3

    while life > 0:
        display.print_map(MAP_SIZE[0], MAP_SIZE[1], player_position)
        button = controls.getch()
        for vector_component in range(len(player_position)):
            player_position[vector_component] += DIRRECTIONS[button][vector_component]
            if player_position[vector_component] == 0 or player_position[vector_component] == MAP_SIZE[vector_component] - 1:
                player_position[vector_component] -= DIRRECTIONS[button][vector_component]
