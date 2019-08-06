"""class Favorite
"""
from database import upload_data, my_cursor, connexion
import mysql.connector
from mysql.connector import errorcode


class Favorite:
    
    def __init__(self):
        self.cursor = my_cursor
    
    def insert_data(self, product_choice, product_substituted, url, grade):
        add_favorite = (
            "INSERT IGNORE INTO Favorite"
            "(product, substitute, lien, grade)"
            " VALUE (%s, %s, %s, %s)"
            )

        data_field = (
            product_choice, product_substituted, url, grade
        )   

        
        my_cursor.execute(add_favorite, data_field)
        connexion.commit()

    def get_all(self):
            pass