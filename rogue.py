import os

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def print_map(x, y, player_position):
    POSITION_X = 0
    POSITION_Y = 1
    os.system('clear')
    map = ''
    for i in range(x):
        for j in range(y):
            if i == 0 or i == y - 1 or j == 0 or j == x - 1: 
                map += '#'
            else:
                if player_position[POSITION_X] == i and player_position[POSITION_Y] == j:
                    map += '@'
                else:
                    map += '.'

        map += '\n'
    print(map)        

def main():
    DIRRECTIONS = {'w': [-1, 0], 's': [1, 0], 'a': [0, -1], 'd': [0, 1]}
    player_position = [3, 3]
    LVL_X = 15
    LVL_Y = 15
    life = 3
    
    while life > 0:
        print_map(LVL_X, LVL_Y, player_position)
        button = getch()
        for vector_component in range(len(player_position)):
            player_position[vector_component] += DIRRECTIONS[button][vector_component]
            if player_position[vector_component] == 0 or player_position[vector_component] == LVL_SIZE - 1:
                player_position[vector_component] -= DIRRECTIONS[button][vector_component]



main()