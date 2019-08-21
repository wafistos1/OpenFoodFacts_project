"""Modul of All fonctions
"""
from constants import data_categories


def validate_entering(start, end):
    """Function that verifies that the user enters an integer between
    a defined interval
    """
    index = None
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
    print("1- Afficher les Favoris( Retrouver mes aliments substitués)")
    print("2- Rechercher un produit( Quel aliment souhaitez-vous remplacer?)")
    print("3- Update la base de donnees(une fois par semaine)")
    print("4- Quitter")
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")


def menu_choice_product():
    """Function that allows to display the products in
    the database according to the choice of the category
    """
    print("-------------------------------------------------------")
    print("****                                               ****")
    print("****   Vous Cherchez un nouveau produit            ****")
    print("****   Choisissez une categorie de produit         ****")
    print("****                                               ****")
    print("-------------------------------------------------------")
    for cle in data_categories:
        print(f"{cle[0]}- {cle[1]}")
