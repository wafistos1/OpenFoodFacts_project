"""Class product
"""
from database import upload_data, my_cursor
import mysql.connector
from mysql.connector import errorcode


class Product:

    def __init__(self):
        self.cursor = my_cursor 
        self.choise_product = 0
        self.list_posting = []            
    # Method that displays the products of the category the user has chosen
    def get_product(self, index):

        query = (" SELECT `name`, `grade` FROM `Product`"
                " WHERE `id_category` = %s "
        )
        self.cursor.execute(query, (index, ))
        i = 1
        print(self.list_posting)
        for name in self.cursor:
            self.list_posting.append(name)
            print(f"{i}-{self.list_posting[i-1][0]}")
            i += 1
        self.choise_product = int(input("Veuillez choisir un produit SVP: "))
        print(f"Vous avez choisie {self.list_posting[self.choise_product-1][0].upper()} avec grade: {self.list_posting[self.choise_product-1][1].upper()}")

    # Method that displays substitus products
    def search_product(self, index_category):

        query =("SELECT `*` FROM `Product`"
                "INNER JOIN `Category`"
                    "ON Product.id_category = Category.id "
                "WHERE Product.grade < %s"
                "AND Category.id = %s "
                "LIMIT 10"
            )
        
        index = self.list_posting[self.choise_product-1][1]

        self.cursor.execute(query, (index, index_category))

        for name in self.cursor:
            if name[1] == None:
                print("Votre produit a le meilleur grade dans notre base de donnees")
            else:
                print(f"{name[1]} avec grade: {name[3].upper()} lien Url: ")

        
    
