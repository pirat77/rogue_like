import os
os.system('clear')


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


def display(hero_pos_x, hero_pos_y):
    height = 20
    width = 20
    field = []
    for y in range(height):
        line = []
        for x in range(width):
            if y == 0 or y == height-1 or x == 0 or x == width-1:
                line.append("#")
            elif y == hero_pos_y and x == hero_pos_x:
                line.append("@")
            else:
                line.append(".")
        field.append(line)
    field_string = ""
    for element in field:
        field_string += "".join(element) + "\n"
    return field_string


print(display(12,17))


buttons_dict = {"w": [-1, 0], "s": [1, 0], "a": [0, -1], "d": [0, 1]}


button = getch()
