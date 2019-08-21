""" Script to .....
"""
import os
import platform
from sql import check_database, data_init
from constants import clear
from fonctions import validate_entering, menu_main
from choice import ChoiceMenu


def main():
    """ main fonction to start a script
    """
    platform.system()
    # Initialisation data (upload json file from api)
    if check_database():
        data_init()

    # Main loop
    while True:
        print(clear)
        os.system(clear)
        menu_main()
        switcher = {
            1: ChoiceMenu.favorite_poster,
            2: ChoiceMenu.product_poster,
            3: ChoiceMenu.update_data,
            4: ChoiceMenu.quitter
            }
        index = validate_entering(1, 4)
        switcher[index]()
        if index == 4:
            break
    print("                                                       ")
    print("-------------------------------------------------------")
    print("Aurevoir...")


if __name__ == "__main__":
    main()
