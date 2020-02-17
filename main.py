import controls
import os
import display
import common_functions


def main():
    display.welcome()


def print_map(x, y, player_position):
    POSITION_X = 0
    POSITION_Y = 1
    os.system('clear')
    map = ''
    for i in range(x):
        for j in range(y):
            if i == 0 or i == x - 1 or j == 0 or j == y - 1:
                map += '#'
            else:
                if player_position[POSITION_X] == i and player_position[POSITION_Y] == j:
                    map += '@'
                else:
                    map += '.'

        map += '\n'
    print(map)


def moving_on_map():
    DIRRECTIONS = {'w': [-1, 0], 's': [1, 0], 'a': [0, -1], 'd': [0, 1]}
    player_position = [3, 3]
    MAP_SIZE = [15, 15]
    life = 3

    while life > 0:
        print_map(MAP_SIZE[0], MAP_SIZE[1], player_position)
        button = controls.getch()
        for vector_component in range(len(player_position)):
            player_position[vector_component] += DIRRECTIONS[button][vector_component]
            if player_position[vector_component] == 0 or player_position[vector_component] == MAP_SIZE[vector_component] - 1:
                player_position[vector_component] -= DIRRECTIONS[button][vector_component]


main()