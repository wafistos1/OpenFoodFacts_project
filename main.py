""" Script to .....
"""
from product import Product
from favori import Favorite
from database import upload_data
from sql import *
from constants import * 


def main():
    """ main fonction for start a script
    """
    check_database()
    print(data_exist)
    
    # Initialisation our data (upload json file from api)
    if data_exist == True:
        data_init()
        

    exit_script = 'Oui'
    while exit_script == 'Oui':
        print("-------------------------------------------------------")
        print("-------------------------------------------------------")
        print("****   Bienvenue dans le programme openfood        ****")
        print("-------------------------------------------------------")
        print("-------------------------------------------------------")
        print("****   Vous voulez Choisir un element du favori?   ****")
        print("****   (Oui / Non)                                 ****")
        print("-------------------------------------------------------")
        print("****   Vous Cherchez un nouveau produit            ****")
        print("****   Choisissez une categorie de produit         ****")
        print("-------------------------------------------------------")
        print("1- Boissons")
        print("2- Produits laitiers")
        print("3- biscuits")
        print("4- Petit-déjeuners")
        print("5- Plats préparés")
        print("6- Produits à tartiner")
        print("-------------------------------------------------------")
        index_choice = None
        while index_choice not in [1, 2, 3, 4, 5, 6]:
            try:
                index_choice = int(input("Entrez votre choix SVP: "))
            except ValueError:
                continue

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
        print(produit.list_favorite)
        favorite = Favorite()
        favorite.insert_data(
            produit.list_favorite[1][0], 
            produit.list_favorite[0][1],
            produit.list_favorite[0][2], 
            produit.list_favorite[0][3]
        )
        print("-------------------------------------------------------")
        print("Voulez vous continuez (Oui / Non)")
        exit_script = input("Entrez votre choix: ").capitalize()
        
    print("Aurevoir")

if __name__ == "__main__":
    main()
