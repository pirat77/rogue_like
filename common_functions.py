import display
import controls


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


def explore_menu():
    pass


distribute_stat_points()
