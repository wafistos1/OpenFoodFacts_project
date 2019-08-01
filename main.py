""" Script to .....
"""
from product import Product
from database import upload_data
from sql import *
from constants import * 


def main():
    """ main fonction for start a script
    """
    
    # Initialisation our data (upload json file from api)
    data_init()

    exit_script = 'Non'
    while exit_script == 'Non':
        print("****   Bienvenue dans le programme openfood        ****")
        print("****   Vous voulez Choisir un element du favori?   ****")
        print("****   Oui / Non                                   ****")
        print("****   Vous Cherchez un nouveau produit            ****")
        print("****   Choisissez une categorie de produit         ****")
        print("-------------------------------------------------------")
        print("1- Boissons")
        print("2- Produits laitiers")
        print("3- Chocolats")
        print("-------------------------------------------------------")
        index_choice = input("Entrez votre choix SVP: ")
        produit = Product()
        print("-------------------------------------------------------")
        print("Veuillez patienter...")
        print("-------------------------------------------------------")
        print("Liste des produits disponible")
        print("-------------------------------------------------------")
        produit.get_product(index_choice)
        print("-------------------------------------------------------")
        produit.search_product(index_choice)
        print("-------------------------------------------------------")
        print("Voulez vous continuez ou Non")
        exit_script = input("Entrez votre choix: ").capitalize()
        print(exit_script)
    print("Aurevoir")

if __name__ == "__main__":
    main()
