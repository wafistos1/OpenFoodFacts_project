"""Class product of table with same name
"""
from database import my_cursor, connexion


class Product:
    """Class that represents the Product table
    """

    def __init__(self):
        self.cursor = my_cursor
        self.list_posting = []
        self.list_choice = []

    def create(self):
        """
        Create Product tables
        """
        query = (
            "CREATE TABLE IF NOT EXISTS `Product` ("
            "  `id` SMALLINT NOT NULL AUTO_INCREMENT,"
            "  `name` varchar(450) NOT NULL UNIQUE,"
            "  `url` varchar(450) NOT NULL,"
            "  `grade` varchar(40) ,"
            "  `id_category` SMALLINT NOT NULL ,"
            "  `store` varchar(540) ,"
            "  PRIMARY KEY (`id`),"
            "   CONSTRAINT  `fk_category_id` FOREIGN KEY (`id_category`)"
            "   REFERENCES `Category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE"
            ") ENGINE=InnoDB"
        )
        self.cursor.execute(query)
        connexion.commit()

    def insert_data(self, name, url, grade, id_category, store):
        """
        Method insert data from APi to Product table
        """

        query = (
            "INSERT IGNORE INTO Product "
            "(name, url, grade, id_category, store)"
            "VALUES (%s,  %s, %s, %s, %s)"
        )
        self.cursor.execute(query, (name, url, grade, id_category, store))
        connexion.commit()

    def get_product(self, index):
        """ Method that displays the products of the category the user has chosen
        :return: list of all product from index categorie
        """
        query = (
            " SELECT `id`,`name`, `grade`, `url` FROM `Product`"
            " WHERE `id_category` = %s"
            )

        self.cursor.execute(query, (index, ))
        for name in enumerate(self.cursor):
            self.list_posting.append(name)
        return self.list_posting

    def search_product(self, grade, index_category):
        """ Method that displays substitus products
        :return: List of products of better nutritional quality
        """
        query = (
            "SELECT `*` FROM `Product`"
            "INNER JOIN `Category`"
            "ON Product.id_category = Category.id "
            "WHERE Product.grade < %s"
            "AND Category.id = %s "
            "ORDER BY Product.grade"
            )
        self.cursor.execute(query, (grade, index_category))

        for name in enumerate(self.cursor):
            self.list_choice.append(name)
        return self.list_choice
