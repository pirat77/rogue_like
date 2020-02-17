import display
import controls
import os
import storage


def distribute_stat_points(character={"STR": 10, "CON": 10, "DEX": 10, "INT": 10}, spare_points=10):
    display.display_distribute_stats(spare_points, character)
    cursor_position = 0
    stats_names = ["STR", "CON", "DEX", "INT"]
    while spare_points > 0:
        user_key = controls.getch()
        if user_key == "s" and cursor_position < 3:
            cursor_position += 1
        elif user_key == "w" and cursor_position > 0:
            cursor_position -= 1
        elif user_key == "+":
            character[stats_names[cursor_position]] += 1
            spare_points -= 1
        display.display_distribute_stats(spare_points, character, cursor_position)
    return character


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
