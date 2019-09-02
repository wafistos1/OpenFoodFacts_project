"""Favorite class that inserts the selected products into
the database and can display them
"""
from database import my_cursor, connexion


class Favorite:
    """Favorite class that inserts the selected products into
    the database and can display them
    """
    def __init__(self):
        self.cursor = my_cursor
        self.list_favorite_data = []

    def create(self):
        """
        Method create favorite table
        :return:
        """
        query = (
            "CREATE TABLE IF NOT EXISTS `Favorite` ("
            "  `id` int(11) NOT NULL AUTO_INCREMENT,"
            "   `product` varchar(450) NOT NULL,"
            "   `substitute` varchar(450) NOT NULL,"
            "   `id_product_substitute` SMALLINT NOT NULL,"
            "   `id_product` SMALLINT NOT NULL,"
            "  PRIMARY KEY (`id`),"
            "   CONSTRAINT  `fk_favorite_id` FOREIGN KEY (`id_product_substitute`)"
            "   REFERENCES `Product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,"            
            "   CONSTRAINT  `fk_product_id` FOREIGN KEY (`id_product`)"
            "   REFERENCES `Product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE"
            ") ENGINE=InnoDB"
        )
        self.cursor.execute(query)
        connexion.commit()

    def insert_data(self, product_choice, product_substituted, url, grade, id_substitute):
        """Add the DATA in the favorite table
        """
        add_favorite = (
            "INSERT INTO `Favorite`"
            "(`product`, `substitute`, `lien`, `grade`, `id_product_substitute`)"
            " VALUE (%s, %s, %s, %s, %s)"
            )
        data_field = (
            product_choice, product_substituted, url, grade, id_substitute
        )
        self.cursor.execute(add_favorite, data_field)
        connexion.commit()

    def get_all(self):
        """A method that displays all favorite products with their substitutes
        :return List of all products in favorite table
        """
        self.cursor.execute("SELECT * FROM Favorite")
        for name in enumerate(self.cursor):
            self.list_favorite_data.append(name)
        return self.list_favorite_data

    def empty_favorite(self):
        """
        Method that delete product substitute in table favorite
        """
        query = (
            " truncate `Favorite`"
            )
        self.cursor.execute(query)
        connexion.commit()
