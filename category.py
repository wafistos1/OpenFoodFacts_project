"""class Category
"""
from database import upload_data, my_cursor
import mysql.connector
from mysql.connector import errorcode


class Category:
    
    def __init__(self):
        self.cursor = my_cursor

    def search(self):
        pass

