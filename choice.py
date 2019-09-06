"""Module that groups the static methods of the main menu
"""
import os
from sql import data_init
from fonctions import validate_entering, menu_choice_product, menu_favorite
from constants import clear, data_categories
from app import App


class ChoiceMenu:
    """static methods for menu selection
    """
    list_product_categories = []
    list_best_product_grade = []
    grade_product_choice = None
    index_category = None
    index_grade = None

    @staticmethod
    def favorite_poster():
        """function that displays favorites in the database
        """
        os.system(clear)
        menu_favorite()
        app = App()
        app.display_favorite()
        input("\nAppuyer sur une touche pour continue")

    @staticmethod
    def product_poster():
        """function that displays the products of a category in the database
        """
        os.system(clear)
        menu_choice_product()
        print("-------------------------------------------------------")
        index_category = validate_entering(1, len(data_categories))
        app = App()
        print("-------------------------------------------------------")
        print("Liste des produits disponibles")
        print("                                                       ")
        product_choice = app.display_product_category(index_category)
        grade = product_choice[1][2]
        print("-------------------------------------------------------")
        print("***          Liste des substituts          ***")
        print("-------------------------------------------------------")
        list_best_product_grade = app.display_best_product(grade, index_category)
        if not list_best_product_grade:
            print('Votre produit a le meilleur grade dans la base de donnees')
            app.save_product_substitute(
                product_choice[1][1],
                product_choice[1][1],
                product_choice[1][0],
                product_choice[1][0],
            )
        else:
            print("-------------------------------------------------------")
            choice_subs = validate_entering(1, len(list_best_product_grade))
            os.system(clear)
            print("=======================================================")
            print("Votre produit substitut est: ")
            print(f"{list_best_product_grade[choice_subs][1][1]}")
            print("Grade", end=' ')
            print(f"{list_best_product_grade[choice_subs][1][3]}")
            if list_best_product_grade[choice_subs][1][5] is not None:
                print("-------------------------------------------------------")
                print(f"Disponibles dans le.s magasin.s suivants: ")
                print(f"{list_best_product_grade[choice_subs][1][5]}  ")
            print("-------------------------------------------------------")
            print("Lien Url")
            print("-------------------------------------------------------")
            print(f"{list_best_product_grade[choice_subs][1][2]}")
            print("-------------------------------------------------------")
            print(list_best_product_grade[choice_subs][1][0])
            app.save_product_substitute(
                product_choice[1][1],
                list_best_product_grade[choice_subs][1][1],
                list_best_product_grade[choice_subs][1][0],
                product_choice[1][0],
            )
    @staticmethod
    def update_data():
        """Update my database
        """
        data_init()
        print("Mise a jour terminee")
        os.system('pause')

    @staticmethod
    def quitter():
        """function to exit the program
        """
        print('Vous quittez le programme')
