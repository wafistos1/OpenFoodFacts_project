"""Module that groups the static methods of the main menu
"""
import os
from product import Product
from favori import Favorite
from fonctions import validate_entering, yes_no, menu_favorite, browse_list, browse_favorite
from constants import NUMBER_PRODUCT_PAGE, NUMBER_VAFORITE_PAGE, clear, NUMBER_VAFORITE


class App:
    def __init__(self):
        self.user_choice = None

    def afficher_favorite(self):
        """function that displays favorites in the database
        """
        os.system(clear)
        menu_favorite()
        self.user_choice = int(input("taper votre choix: "))
        favorite1 = Favorite()
        list_favorite = favorite1.get_all()
        if self.user_choice == 1:
            browse_favorite(NUMBER_VAFORITE, list_favorite)
        else:
            favorite1.empty_favorite()
            print('Tous les favoris ont été supprimes')
            input("\nAppuyer sur une touche pour continue")
        self.user_choice = None

    def afficher_produit_categorie(self, index_category): # changer le nom de la methode
        """function that displays the products of a category in the database
        :return List of products in relation to the choice of a category
        """""
        produit = Product()
        list_product_categories = produit.get_product(index_category)
        browse_list(NUMBER_PRODUCT_PAGE, list_product_categories)
        self.user_choice = validate_entering(1, len(list_product_categories))
        os.system(clear)
        print("-------------------------------------------------------")
        print(f"Vous avez choisie {list_product_categories[self.user_choice-1][1][1]}\
            \nGrade: {list_product_categories[self.user_choice-1][1][2]}")
        return list_product_categories[self.user_choice-1]
        self.user_choice = None

    def afficher_best_product(self, grade, category):
        """Method that selects better quality products in relation to a product chosen by the user
        :return List of products best quality products
        """""
        produit = Product()
        list_best_product_grade = produit.search_product(grade, category)
        browse_list(NUMBER_VAFORITE_PAGE, list_best_product_grade)
        return list_best_product_grade

    def enregister_produit_substitut(
            self,
            product_choice,
            product_substitute,
            url,
            grade,
            id_substitute
    ):
        """
        Method save selected product in favorite table in DB
        :param product_choice:
        :param product_substitute:
        :param url:
        :param grade:
        :param id_substitute:
        """

        print("=======================================================")
        print("Voulez vous sauvgarder ce produit? (Oui/Non)")
        print("=======================================================")
        print("                                                       ")
        reponse = yes_no()
        favorite = Favorite()
        if reponse == 'Oui':
            favorite.insert_data(
                product_choice,
                product_substitute,
                url,
                grade,
                id_substitute,
            )
        print("Produit enregistre aux Favoris")
        print("Appuyer sur une touche pour continuer")
        input()
