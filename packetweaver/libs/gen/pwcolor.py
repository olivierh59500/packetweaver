# coding: utf8


class PWColor:
    ENDC = '\033[0m'

    colors = {
        "": '',
        "white": '\033[30m',
        "red": '\033[31m',
        # "green": '\033[32m',
        "orange": '\033[33m',
        "blue": '\033[34m',
        "purple": '\033[35m',
        "cyan": '\033[36m',
        "lightgrey": '\033[37m',
        "darkgrey": '\033[90m',
        "red": '\033[91m',
        "green": '\033[92m',
        "yellow": '\033[93m',
        "blue": '\033[94m',
        "pink": '\033[95m',
        "cyan": '\033[96m',
    }
    effects = {
        "": '',
        "bold": '\033[1m',
        "underline": '\033[4m',
    }
    backgrounds = {
        "white": '\033[40m',
        "red": '\033[41m',
    }

    @staticmethod
    def print_panel():
        """ Display a color message using all available modifiers """
        for c in PWColor.colors.keys():
            print(PWColor.colors[c] + "I am " + str(c) + PWColor.ENDC)
        for c in PWColor.effects.keys():
            print(PWColor.effects[c] + "I am " + str(c) + PWColor.ENDC)
        for c in PWColor.backgrounds.keys():
            print(PWColor.backgrounds[c] + "I am " + str(c) + PWColor.ENDC)

if __name__ == '__main__':
    PWColor.print_panel()
