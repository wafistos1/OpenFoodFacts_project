"""Module that groups the static methods of the main menu
"""
import os
from product import Product
from favori import Favorite
from fonctions import *
from constants import NUMBER_PRODUCT_PAGE, NUMBER_VAFORITE_PAGE, clear, NUMBER_VAFORITE


class App:
    """
    class that groups the different methods that process
    the data in the database
    """
    def __init__(self):
        self.user_choice = None
        self.reponse = None
        self.produit = Product()

    def display_favorite(self):
        """function that displays favorites in the database
        """
        os.system(clear)
        menu_favorite()
        self.user_choice = validate_entering(1, 2)
        favorite1 = Favorite()
        list_favorite = favorite1.get_all()
        if self.user_choice == 1:
            browse_favorite(NUMBER_VAFORITE, list_favorite)
        else:
            favorite1.empty_favorite()
            print('Tous les favoris ont été supprimes')
            os.system('pause')

    def display_product_category(self, index_category): # changer le nom de la methode
        """function that displays the products of a category in the database
        :return List of products in relation to the choice of a category
        """""
        list_product_categories = self.produit.get_product(index_category)
        browse_list(NUMBER_PRODUCT_PAGE, list_product_categories)
        self.user_choice = validate_entering(1, len(list_product_categories))
        os.system(clear)
        print("-------------------------------------------------------")
        print(f"Vous avez choisie {list_product_categories[self.user_choice-1][1][1]}\
            \nGrade: {list_product_categories[self.user_choice-1][1][2]}")
        return list_product_categories[self.user_choice - 1]

    def display_best_product(self, grade, category):
        """Method that selects better quality products in relation to a product chosen by the user
        :return List of products best quality products
        """""
        list_best_product_grade = self.produit.search_product(grade, category)
        browse_list(NUMBER_VAFORITE_PAGE, list_best_product_grade)
        return list_best_product_grade

    def save_product_substitute(
            self,
            product_choice,
            product_substitute,
            id_product_substitute,
            id_product
    ):
        """
        Method save selected product in favorite table in DB
        :param product_choice:First choice product of user
        :param product_substitute:the product that the program has chosen for the user
        :param id_product_substitute:id of product in Product tables(FK)
        :param id_product:id of product in Product tables(FK)
        """
        menu_save()
        self.reponse = yes_no()
        favorite = Favorite()
        if self.reponse == 'Oui':
            favorite.insert_data(
                product_choice,
                product_substitute,
                id_product_substitute,
                id_product
            )
        print("Produit enregistre aux Favoris")
        os.system('pause')
