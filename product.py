"""Class product of table with same name
"""
import mysql.connector
from mysql.connector import errorcode
from database import my_cursor

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


        for i, name in enumerate (self.cursor):
            self.list_posting.append(name)
            print(f"{i+1}-{self.list_posting[i-1][0]}")
            if i % 50 == 0 and i != 0: # Display 50 products at a time
                input("\nAppuyer sur n'importe quel touche les suivants ")
    
        self.choice_product = int(input("Veuillez choisir un produit SVP: "))
        print("-------------------------------------------------------")
        print(f"Vous avez choisie {self.list_posting[self.choice_product-1][0].upper()} avec grade: {self.list_posting[self.choice_product-1][1].upper()}")
        print("-------------------------------------------------------")


    def search_product(self, index_category):
        """ Method that displays substitus products
        """
        query =(
            "SELECT `*` FROM `Product`"
            "INNER JOIN `Category`"
            "ON Product.id_category = Category.id "
            "WHERE Product.grade < %s"
            "AND Category.id = %s "
            "ORDER BY Product.grade"
            )

        index = self.list_posting[self.choice_product-1][1]
        self.cursor.execute(query, (index, index_category))
        
        # Increamentation
        for i, name in enumerate (self.cursor):
            if name is not None:
                print(f"{i+1}-{name[1]} avec grade: {name[3].upper()}")
                self.list_choice.append(name)
                

        if self.list_choice == []:
            print('Votre produit a le meilleur grade dans notre base de donnees!!')
        
        else:
            # Boucle for choice user
            print("-------------------------------------------------------")
            self.choice_subs = int(input("Entrez le numero de votre Produit substitue: "))
            print("-------------------------------------------------------")
            print("Vous produit substitue est : ")
            print("-------------------------------------------------------")
            print(f"{self.list_choice[self.choice_subs-1][1].upper()}")
            print(" De grade")
            print( f"{self.list_choice[self.choice_subs-1][3].upper()} ")
            print("-------------------------------------------------------")
            print(f"Vous trouverai ce produit dans les magasins suivants: ")
            print("-------------------------------------------------------")
            print(f"{self.list_choice[self.choice_subs-1][5].upper()}  ")
            print("-------------------------------------------------------")
            print("Lien Url")
            print("---------")
            print(f"{self.list_choice[self.choice_subs-1][2]}")
            print("-------------------------------------------------------")
            if self.list_choice == []: # If our choice as the best grade
                # Add the selected product to the favorite lis
                self.list_favorite.append(self.list_posting[self.choice_product])
            else:
                self.list_favorite.append(self.list_choice[self.choice_subs-1])
                self.list_favorite.append(self.list_posting[self.choice_product-1])

