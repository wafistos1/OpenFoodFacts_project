"""Favorite class that inserts the selected products into 
the database and can display them 
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
        self.cursor.execute(add_favorite, data_field)
        connexion.commit()


    def get_all(self):
        """A method that displays all favorite products with their substitutes
        """
        self.cursor.execute("SELECT * FROM Favorite" )
        for i, name in enumerate (self.cursor):
            print(f"{i+1}-{name[1].upper()} son substitu est: {name[2].upper()}")
            print(f"De grade {name[4].upper()}" )
        connexion.commit()