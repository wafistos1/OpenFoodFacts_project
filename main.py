""" Script to .....
"""
from product import Product
from category import Category
from database import upload_data


def main():
    """ main fonction for start script
    """
    json_data = upload_data()
    produit = Product()
    produit.create_table()

    print("****     Bienvenue dans le programme openfood      ****")
    print("****   Vous voulez Choisir un element du favori?   ****")
    print("****                     Oui / Non                 ****")
    print("****       Vous Cherchez un nouveau produit        ****")

if __name__ == "__main__":
    main()
