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
    for i in range(height):
        line = []
        for j in range(width):
            if i == 0 or i == height-1 or j == 0 or j == width-1:
                line.append("#")
            elif i == hero_pos_y and j == hero_pos_x:
                line.append("@")
            else:
                line.append(".")
        field.append(line)
    field_string = ""
    for element in field:
        field_string += "".join(element) + "\n"
    return field_string


print(display(12,17))


buttons_dict = {"w": [-1,]}


x = getch()
while x !="x":
    x = getch()
    print(x)
