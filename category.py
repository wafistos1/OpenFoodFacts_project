"""Favorite class that inserts the selected products into
the database and can display them
"""
from database import my_cursor, connexion
from constants import data_categories


class Category:
    """
    Class Category that create ans insert data in category table
    """
    def __init__(self):
        self.cursor = my_cursor

    def create(self):
        """
        Create categry table in database
        """
        query = (
            "CREATE TABLE IF NOT EXISTS `Category` ("
            "   `id` SMALLINT NOT NULL AUTO_INCREMENT,"
            "   `name` varchar(450) NOT NULL,"
            "   PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB"
        )
        self.cursor.execute(query)
        connexion.commit()

    def insert_data(self):
        """
        Insert data from categories list in category table
        """
        query2 = (
            "INSERT IGNORE INTO Category (id, name) VALUE (%s, %s)"
        )
        for name_categorie in data_categories:
            self.cursor.execute(query2, (name_categorie[0], name_categorie[1]))
            connexion.commit()
