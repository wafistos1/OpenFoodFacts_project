"""class Favorite
"""
from database import upload_data, my_cursor
import mysql.connector
from mysql.connector import errorcode


class Favorite:
    
    def __init__(self):
        self.cursor = my_cursor
    
    def insert_data(self, product_name, choice_name):
        pass

    def search(self):
        pass