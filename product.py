"""Class product
"""
from database import upload_data, my_cursor
import mysql.connector
from mysql.connector import errorcode

DATA = upload_data()

class Product:
    def __init__(self):
        self.cursor = my_cursor              


    def search(self):
        pass
    
    

