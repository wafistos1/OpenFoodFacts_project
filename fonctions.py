"""Modul of All fonctions
"""
from constants import data_categories


def validate_entering(start, end):
    """Function that verifies that the user enters an integer between
    a defined interval
    """
    while True:
        try:
            index = int(input('Entrez votre choix: '))
            assert start <= index <= end
        except ValueError:
            print('SVP entrez un entier valide')
        except AssertionError:
            print(f"SVP entrez un entier entre [{start}-{end}]")
        else:
            break

    return index


def yes_no():
    """Function that allows to check that the user enters'Oui' or'Non'
    """
    index = None
    while index not in ['Oui', 'Non']:
        try:
            index = str(input('Entrez votre choix:(Oui/Non) ').capitalize())
        except ValueError:
            print('SVP entrez un mot valide')
    return index


def menu_main():
    """Function to display the main menu
    """
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")
    print("****                                               ****")
    print("****   Bienvenue dans le programme OPENFOOD        ****")
    print("****                                               ****")
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")
    print("1- Afficher les Favoris(Retrouver mes aliments substitués)")
    print("2- Rechercher un produit(Quel aliment remplacer?)")
    print("3- Update la base de donnees(une fois par semaine)")
    print("4- Quitter")
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")


def menu_choice_product():
    """Function that allows to display the products in
    the database according to the choice of the category
    """
    print("-------------------------------------------------------")
    print("****            MENU RECHERCHE                     ****")
    print("****   Vous Cherchez un nouveau produit            ****")
    print("****   Choisissez une categorie de produit         ****")
    print("****                                               ****")
    print("-------------------------------------------------------")
    for cle in data_categories:
        print(f"{cle[0]}- {cle[1]}")


def menu_favorite():
    """Function that display the favorite table
    """
    print("---------------------------------------------")
    print("****         MENU FAVORIS                ****")
    print("**** 1- Afficher les favoris?            ****")
    print("**** 2- Supprimer tous les favoris?      ****")
    print("---------------------------------------------")


def browse_list(number_product, list_product):
    """
    Fuction to browse list and poster product
    :param number_product:
    :param list_product:
    :return:
    """
    for i, product in enumerate(list_product):
        print(f'{i + 1}- {product[1][1]}')
        if i % number_product == 0 and i != 0:  # Display 50 products at a time
            key = input("\nAppuyer sur n'importe quelle touche les suivants \
            \nAppuyer sur Q si vous avez tourvez votre choix ").capitalize()
            if key == 'Q':
                break


def browse_favorite(number_favorite, list_favorite):
    """
    Function to browse favorite in Favorite database and poster all products
    :param number_favorite:
    :param list_favorite:
    :return:
    """
    print("=============================================================")
    print("                 Liste des Favoris                           ")
    print("=============================================================")

    for i, name in enumerate(list_favorite):
        print(f"{i + 1}-PRODUIT:{name[1][1]} \n-SUBSTITUT:{name[1][2]} ")
        print("---------------------------------------------------------")
        if i % number_favorite == 0 and i != 0:
            input("\nAppuyer sur une touche pour continue")


def menu_save():
    print("=======================================================")
    print("Voulez vous sauvgarder ce produit? (Oui/Non)")
    print("=======================================================")
    print("                                                        ")