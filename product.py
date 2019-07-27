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
        for name in self.cursor:
            print(f"{i}-{name}")
            i += 1
        
