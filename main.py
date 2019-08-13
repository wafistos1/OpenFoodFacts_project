""" Script to .....
"""
import os
from sql import check_database, data_init
from constants import validate_entering, menu_main, CLEAR
from fonctions import favorite_poster, product_poster, update_data, quitter
def main():
    """ main fonction to start a script
    """
    # Initialisation our data (upload json file from api)
    if check_database():
        data_init()
    #Check os system
    print("Votre systeme operationnel")
    print("1- Linux ou Mac")
    print("2- Windows")
    CLEAR = validate_entering(1, 2)
    if CLEAR == 1:
        CLEAR = 'clear'
    else:
        CLEAR = 'cls'
    
    #Main loop
    while True:
        os.system(CLEAR)
        menu_main()
        index = None
        switcher = {
            1: favorite_poster,
            2: product_poster,
            3: update_data,
            4: quitter
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
