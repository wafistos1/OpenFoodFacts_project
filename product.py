"""Class product
"""
import mysql.connector
from mysql.connector import errorcode
from database import upload_data, my_cursor

class Product:

    def __init__(self):
        self.cursor = my_cursor
        self.choice_product = 0
        self.choice_subs = 0
        self.list_posting = []
        self.list_choice = []
    # Method that displays the products of the category the user has chosen
    def get_product(self, index):

        query = (" SELECT `name`, `grade` FROM `Product`"
                " WHERE `id_category` = %s ")

        self.cursor.execute(query, (index, ))
        i = 1
        print(self.list_posting)
        for name in self.cursor:
            self.list_posting.append(name)
            print(f"{i}-{self.list_posting[i-1][0]}")
            i += 1
        self.choice_product = int(input("Veuillez choisir un produit SVP: "))
        print("-------------------------------------------------------")
        print(f"Vous avez choisie {self.list_posting[self.choice_product-1][0].upper()} avec grade: {self.list_posting[self.choice_product-1][1].upper()}")
        print("-------------------------------------------------------")

    # Method that displays substitus products
    def search_product(self, index_category):

        query =("SELECT `*` FROM `Product`"
                "INNER JOIN `Category`"
                    "ON Product.id_category = Category.id "
                "WHERE Product.grade < %s"
                "AND Category.id = %s "
                "LIMIT 10")

        index = self.list_posting[self.choice_product-1][1]

        self.cursor.execute(query, (index, index_category))
        i = 1 # Increamentation 
        for name in self.cursor:
            
            if not name:
                print("Votre produit a le meilleur grade dans notre base de donnees")
            else:
                print(f"{i}-{name[1]} avec grade: {name[3].upper()} lien Url: ")
                self.list_choice.append(name)
                i += 1
        
        # Boucle for choice user
        self.choice_subs = int(input("Entrez le numero de votre Produit substitue: "))
        print("-------------------------------------------------------")
        print("Vous produit substitue est : ") 
        print(f"{self.list_choice[self.choice_subs-1][1].upper()}")          
        print("-------------------------------------------------------")
