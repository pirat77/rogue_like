import sys
import display
import time


def load_avatar_from_file(hero_name):
    PATH = sys.argv[0].strip("comming_closer.py")
    file_name = f"{PATH}saves/{hero_name}_avatar.txt"
    with open(file_name, "r") as f:
        loaded_avatar = f.read()
        hero_avatar_loaded = loaded_avatar.split("\n")
    return hero_avatar_loaded


def comming_closer():
    avatar = (load_avatar_from_file('snake'))
    avatar1 = downsize_avatar(avatar)
    avatar2 = downsize_avatar(avatar1)
    avatar3 = downsize_avatar(avatar2)
    display.main_display(avatar3, '')
    time.sleep(0.5)
    display.main_display(avatar2, '')
    time.sleep(0.5)
    display.main_display(avatar1, '')
    time.sleep(0.5)
    display.main_display(avatar, '')


def downsize_avatar(avatar):
    avatar1 = []
    value_dict = {'█': 1.0, '─': 0.0, '░': 0.25, '▀': 0.75, '▄': 0.75, ' ': 0.0, '@': 0.5, '|': 0.25, '=': 0.5, '<': 0.25, '>': 0.25, 'O': 0.5}
    field_list = [' ', '─', '░', '▀', '█']
    for x in range(int(len(avatar)//2)):
        line = ''
        for y in range(int(len(avatar[0])//2)):
            field_value = value_dict[avatar[int(2*x)][int(2*y)]] + value_dict[avatar[int(2*x)][int(2*y+1)]] + value_dict[avatar[int(2*x+1)][int(2*y)]] + value_dict[avatar[int(2*x+1)][int(2*y+1)]]
            line += field_list[int((field_value)//1)]
        avatar1.append(line)
    return avatar1


def main():
    comming_closer()


main()