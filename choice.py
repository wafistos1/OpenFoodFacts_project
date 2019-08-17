"""Module that groups the static methods of the main menu
"""
import os
from product import Product
from favori import Favorite
from sql import data_init
from constants import clear
from fonctions import validate_entering, yes_no, menu_choice_product

class ChoiceMenu:
    """static methods for menu selection
    """
    @staticmethod
    def favorite_poster():
        """function that displays favorites in the database
        """
        os.system(clear)
        print("****                 Favoris               ****")
        print("****                                       ****")
        print("-----------------------------------------------")
        favorite1 = Favorite()
        favorite1.get_all()
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
        print("***          Liste des produits substituts          ***")
        #os.system(clear)
        print("-------------------------------------------------------")
        produit.search_product(index_choice)
        print("=======================================================")
        print("Voulez vous sauvgarde ce produit? (Oui/Non)")
        print("                                                       ")
        reponse = yes_no()
        if reponse == 'Oui' and produit.list_choice != []:
            favorite = Favorite()
            favorite.insert_data(
                produit.list_favorite[1][0],
                produit.list_favorite[0][1],
                produit.list_favorite[0][2],
                produit.list_favorite[0][3],
            )
            print("Produit enregiste aux Favoris")

        elif reponse == 'Oui' and produit.list_choice == []:
            favorite = Favorite()
            favorite.insert_data(
                produit.list_favorite[0][0],
                produit.list_favorite[0][0],
                'none',
                produit.list_favorite[0][1],
            )
            print("Produit enregiste aux Favoris")
        else:
            print("Produit non-enregiste aux Favoris")
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
        print('Vous quitter le programme?')
