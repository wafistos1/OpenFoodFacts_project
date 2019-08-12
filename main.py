""" Script to .....
"""
import os
from sql import check_database, data_init
from constants import validate_entering, yes_no, menu_main, menu_choice_product
from fonctions import favorite_poster, product_poster, update_data, quitter
def main():
    """ main fonction to start a script
    """
    # Initialisation our data (upload json file from api)
    if check_database():
        data_init()
    #Main loop
    while True:
        os.system("clear")
        menu_main()
        index = None
        switcher = {
        1: favorite_poster,
        2: product_poster,
        3: update_data,
        4: quitter,
        }
        index = validate_entering(1, 4)
        switcher[index]()
        if switcher[index]() == 'Oui':
            break
        print("                                                       ")
        print("-------------------------------------------------------")

    print("Aurevoir...")


if __name__ == "__main__":
    main()
