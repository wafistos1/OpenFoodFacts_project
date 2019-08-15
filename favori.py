"""Favorite class that inserts the selected products into
the database and can display them
"""
from database import my_cursor, connexion
from constants import NUMBER_VAFORITE

class Favorite:
    """Favorite class that inserts the selected products into
    the database and can display them
    """
    def __init__(self):
        self.cursor = my_cursor

    def insert_data(self, product_choice, product_substituted, url, grade):
        """Add the DATA in the favorite table
        """
        add_favorite = (
            "INSERT INTO `Favorite`"
            "(`product`, `substitute`, `lien`, `grade`)"
            " VALUE (%s, %s, %s, %s)"
            )
        data_field = (
            product_choice, product_substituted, url, grade,
        )
        self.cursor.execute(add_favorite, data_field)
        connexion.commit()

    def get_all(self):
        """A method that displays all favorite products with their substitutes
        """
        self.cursor.execute("SELECT * FROM Favorite")
        for i, name in enumerate(self.cursor):
            print('-------------------------------------------------------------')
            print(f"{i+1}-{name[1].upper()} son substitut est: {name[2].upper()}")
            print(f"De grade {name[4].upper()}")
            print('-------------------------------------------------------------')
            if i % NUMBER_VAFORITE == 0 and i != 0:
                input("\nAppuyer sur une touche pour continue")
        connexion.commit()
