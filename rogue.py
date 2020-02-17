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
    os.system('clear')
    map = ''
    for i in range(x):
        for j in range(y):
            if i == 0 or i == y - 1 or j == 0 or j == x - 1: 
                map += '#'
            else:
                if player_position[0] == i and player_position[1] == j:
                    map += '@'
                else:
                    map += '.'

        map += '\n'
    print(map)        


def main():
    DIRRECTIONS = {'w': [-1, 0], 's': [1, 0], 'a': [0, -1], 'd': [0, 1]}
    player_position = [3, 3]
    LVL_SIZE = 15
    life = 3
    
    while life > 0:
        print_map(LVL_SIZE, LVL_SIZE, player_position)
        button = getch()
        for x in range(len(player_position)):
            player_position[x] += DIRRECTIONS[button][x]
            if player_position[x] == 0 or player_position[x] == LVL_SIZE - 1:
                player_position[x] -= DIRRECTIONS[button][x]


main()