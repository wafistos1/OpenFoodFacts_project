"""Module that groups the static methods of the main menu
"""
import os
from product import Product
from favori import Favorite
from sql import data_init
from constants import clear
from fonctions import validate_entering, yes_no, menu_choice_product, menu_favorite


class ChoiceMenu:
    """static methods for menu selection
    """
    @staticmethod
    def favorite_poster():
        """function that displays favorites in the database
        """
        os.system(clear)
        menu_favorite()
        choice_user = int(input("entez un chiffre: "))
        favorite1 = Favorite()
        if choice_user == 1:
            favorite1.get_all()
        else:
            favorite1.empty_favorite()
            print('Tous les favoris ont été supprimes')

        input()

    @staticmethod
    def product_poster():
        """function that displays the products of a category in the database
        """
        os.system(clear)
        menu_choice_product()
        print("                                                       ")
        print("-------------------------------------------------------")
        index_choice = None
        index_choice = validate_entering(1, 6)
        produit = Product()
        print("-------------------------------------------------------")
        print("                                                       ")
        print("Liste des produits disponibles")
        print("                                                       ")
        print("-------------------------------------------------------")
        produit.get_product(index_choice)
        print("                                                       ")
        print("-------------------------------------------------------")
        print("***          Liste des substituts          ***")
        print("-------------------------------------------------------")
        produit.search_product(index_choice)
        print("=======================================================")
        print("Voulez vous sauvgarder ce produit? (Oui/Non)")
        print("                                                       ")
        reponse = yes_no()
        if reponse == 'Oui' and produit.list_choice != []:
            favorite = Favorite()
            favorite.insert_data(
                produit.list_favorite[1][0],
                produit.list_favorite[0][1],
                produit.list_favorite[0][2],
                produit.list_favorite[0][3],
                produit.list_favorite[0][0],

            )
            print("Produit enregistre aux Favoris")

        elif reponse == 'Oui' and produit.list_choice == []:
            favorite = Favorite()
            favorite.insert_data(
                produit.list_favorite[0][0],
                produit.list_favorite[0][0],
                'none',
                produit.list_favorite[0][1],
                produit.list_favorite[0][0],

            )
            print("Produit enregistre aux Favoris")
        else:
            print("Produit non-enregistre aux Favoris")
        print("Appuyer sur une touche pour continuer")
        input()

    @staticmethod
    def update_data():
        """Update my database
        """
        data_init()
        print("Mise a jour terminee")
        input()

    @staticmethod
    def quitter():
        """function to exit the program
        """
        print('Vous quittez le programme')
