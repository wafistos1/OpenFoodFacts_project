""" Script to .....
"""
import os
from sql import check_database, data_init
from constants import CLEAR
from fonctions import validate_entering, menu_main
from choice import Choice_menu 
import platform


def main():
    """ main fonction to start a script
    """
    platform.system()
    # Initialisation data (upload json file from api)
    if check_database():
        data_init()
    #Check os system
    if platform.system() == 'Linux' or platform.system() == '':
        CLEAR = 'clear'
    else:
        CLEAR = 'cls'
    
    #Main loop
    while True:
        os.system(CLEAR)
        menu_main()
        index = None
        switcher = {
            1: Choice_menu.favorite_poster,
            2: Choice_menu.product_poster,
            3: Choice_menu.update_data,
            4: Choice_menu.quitter
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
