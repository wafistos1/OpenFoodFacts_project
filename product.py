"""Class product of table with same name
"""
import os
from database import my_cursor
from constants import NUMBER_PRODUCT_PAGE, NUMBER_VAFORITE_PAGE, clear
from fonctions import validate_entering


class Product:
    """Class that represents the Product table
    """

    def __init__(self):
        self.cursor = my_cursor
        self.choice_product = 0
        self.choice_subs = 0
        self.list_posting = []
        self.list_choice = []
        self.list_favorite = []

    def get_product(self, index):
        """ Method that displays the products of the category the user has chosen
        """
        query = (
            " SELECT `name`, `grade` FROM `Product`"
            " WHERE `id_category` = %s"
            )

        self.cursor.execute(query, (index, ))
        for i, name in enumerate(self.cursor):
            self.list_posting.append(name)
            print(f"{i+1}-{self.list_posting[i][0]}")
            if i % NUMBER_PRODUCT_PAGE == 0 and i != 0: # Display 50 products at a time
                key = input("\nAppuyer sur n'importe quelle touche les suivants \
                \nQ si vous avez tourvez votre choix ").capitalize()
                if key == 'Q':
                    break
        self.choice_product = validate_entering(1, len(self.list_posting))
        os.system(clear)
        print("-------------------------------------------------------")
        print(f"Vous avez choisie {self.list_posting[self.choice_product-1][0].upper()} \
            grade: {self.list_posting[self.choice_product-2][1].upper()}")
        print("-------------------------------------------------------")

    def search_product(self, index_category):
        """ Method that displays substitus products
        """
        query = (
            "SELECT `*` FROM `Product`"
            "INNER JOIN `Category`"
            "ON Product.id_category = Category.id "
            "WHERE Product.grade < %s"
            "AND Category.id = %s "
            "ORDER BY Product.grade"
            )
        index = self.list_posting[self.choice_product-2][1]
        self.cursor.execute(query, (index, index_category))
        # Increamentation
        for i, name in enumerate(self.cursor):
            if name is not None:
                print(f"{i+1}-{name[1]} avec grade: {name[3].upper()}")
                self.list_choice.append(name)
                if i % NUMBER_VAFORITE_PAGE == 0 and i != 0:
                    break
        if self.list_choice == []:
            print('Votre produit a le meilleur grade dans notre base de donnees')
            self.list_favorite.append(self.list_posting[self.choice_product-1])
        else:
            # Boucle for choice user
            print("-------------------------------------------------------")
            self.choice_subs = validate_entering(1, len(self.list_choice))
            os.system(clear)
            print("-------------------------------------------------------")
            print("Vous produit substitue est: ")
            print("-------------------------------------------------------")
            print(f"{self.list_choice[self.choice_subs-1][1].upper()}")
            print("De grade", end=' ')
            print(f"{self.list_choice[self.choice_subs-1][3].upper()}")
            if self.list_choice[self.choice_subs-1][5] is not None:
                print("-------------------------------------------------------")
                print(f"Disponibles dans le.s magasin.s suivants: ")
                print(f"{self.list_choice[self.choice_subs-1][5].upper()}  ")
            print("-------------------------------------------------------")
            print("Lien Url")
            print("---------")
            print(f"{self.list_choice[self.choice_subs-1][2]}")
            print("-------------------------------------------------------")
            self.list_favorite.append(self.list_choice[self.choice_subs-1])
            self.list_favorite.append(self.list_posting[self.choice_product-1])
