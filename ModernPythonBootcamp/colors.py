from termcolor import colored
from pyfiglet import figlet_format

valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')


def print_art(msg, color):
    if color not in valid_colors:
        color = 'magenta'
    art = figlet_format(msg, font='standard')
    color_art = colored(art, color=color)
    print(color_art)


msg = input("What message do you want to print?")
color = input("What color?")
print_art(msg, color)
