"""Class product
"""
from database import upload_data, my_cursor
import mysql.connector
from mysql.connector import errorcode


class Product:

    def __init__(self):
        self.cursor = my_cursor              

    def get_product(self, index):

        query = (" SELECT `name` FROM `Product`"
                " WHERE `id_category` = %s "
        )
        self.cursor.execute(query, (index, ))
        i = 1
        list_posting = []
        choise_product = 0
        for name in self.cursor:
            list_posting.append(name[0])
            print(f"{i}-{list_posting[i-1]}")
            i += 1
        choise_product = int(input("Veuillez choisir un produit SVP: "))
        print(f"Vous avez choisie {list_posting[choise_product-1].upper()}")
        
