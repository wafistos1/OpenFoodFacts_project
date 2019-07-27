""" Script to .....
"""
from product import Product
from category import Category
from database import upload_data
from sql import * 


def main():
    """ main fonction for start a script
    """
    data = data_init()

    print("****   Bienvenue dans le programme openfood       ****")
    print("****   Vous voulez Choisir un element du favori?   ****")
    print("****   Oui / Non                                   ****")
    print("****   Vous Cherchez un nouveau produit            ****")
    print("****   Choisissez une categorie de produit         ****")
    print("-------------------------------------------------------")
    print("1- Boissons")
    print("2- Produits laitiers")
    print("3- Chocolats")
    print("-------------------------------------------------------")
    index = input("Entrez votre choix SVP: ")
    produit = Product()
    print("-------------------------------------------------------")
    print("Veuillez patienter...")
    print("-------------------------------------------------------")
    print("Liste des produits disponible")
    print("-------------------------------------------------------")
    produit.get_product(index)
    print("-------------------------------------------------------")


if __name__ == "__main__":
    main()
