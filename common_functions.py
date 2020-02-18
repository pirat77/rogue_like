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


def moving_on_map(map_size, hero_position):
    DIRRECTIONS = {'w': [-1, 0], 's': [1, 0], 'a': [0, -1], 'd': [0, 1]}
    player_position = hero_position
    button = controls.getch()
    if button == '+':
        return player_position, True
    for vector_component in range(len(player_position)):
        if not ((player_position[vector_component] + DIRRECTIONS[button][vector_component] == -1)  or (player_position[vector_component] + DIRRECTIONS[button][vector_component] == map_size[vector_component])):
            player_position[vector_component] += DIRRECTIONS[button][vector_component]        
    return player_position, False